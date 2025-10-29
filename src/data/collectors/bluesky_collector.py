#!/usr/bin/env python3
"""
Bluesky Collector - Weak Signal Detector
----------------------------------------
Non-blocking version with safe 5-minute rate-limit cooldown.
"""

import os
import time
import requests
import re
from datetime import datetime, timezone
from collections import defaultdict, deque
from src.data.threat_keywords import THREAT_KEYWORDS, URGENCY_INDICATORS


class BlueskyCollector:
    """Weak-signal Bluesky collector that polls for French and German posts safely."""

    last_rate_limit = 0  # shared timestamp of last 429 hit
    cooldown_seconds = 300  # 5 minutes

    def __init__(self, language="fr", limit=20):
        self.language = language
        self.limit = limit
        self.api_url = "https://bsky.social"
        self.username = os.getenv("BLUESKY_USERNAME", "")
        self.password = os.getenv("BLUESKY_APP_PASSWORD", "")
        self.jwt_token = None

        # Weak-signal burst detection
        self.recent_mentions = defaultdict(lambda: deque(maxlen=50))
        self.window_seconds = 120  # 2-minute window
        self.clean_re = re.compile(r"<[^>]+>")

        print(f"✅ BlueskyCollector initialized for language={language}")
        self._authenticate()

    # ------------------------------------------------------------------
    def _authenticate(self):
        """Authenticate with Bluesky API and get a session token."""
        if time.time() - BlueskyCollector.last_rate_limit < self.cooldown_seconds:
            remaining = int(self.cooldown_seconds - (time.time() - BlueskyCollector.last_rate_limit))
            print(f"⏭️ Skipping Bluesky authentication (cooldown {remaining}s left).")
            return

        try:
            payload = {"identifier": self.username, "password": self.password}
            r = requests.post(
                f"{self.api_url}/xrpc/com.atproto.server.createSession",
                json=payload,
                timeout=10,
            )
            if r.status_code == 429:
                print("⚠️ Bluesky rate limit hit — skipping for 5 minutes.")
                BlueskyCollector.last_rate_limit = time.time()
                return
            r.raise_for_status()
            data = r.json()
            self.jwt_token = data.get("accessJwt")
            print("🔑 Bluesky session authenticated")
        except Exception as e:
            print(f"❌ Bluesky authentication failed: {e}")
            self.jwt_token = None

    def _headers(self):
        return {"Authorization": f"Bearer {self.jwt_token}"} if self.jwt_token else {}

    # ------------------------------------------------------------------
    def _clean_text(self, text: str) -> str:
        text = re.sub(r"http\S+", "", text)
        text = self.clean_re.sub("", text)
        return text.strip()

    def _compute_signal_score(self, text: str) -> float:
        lang = self.language
        score = 0
        text_lower = text.lower()

        for category, data in THREAT_KEYWORDS.get(lang, {}).items():
            if any(k in text_lower for k in data["keywords"]):
                base = {"low": 1, "medium": 2, "high": 3, "critical": 4}[data["risk_level"]]
                score += base

        if any(u in text_lower for u in URGENCY_INDICATORS.get(lang, [])):
            score *= 1.5
        if any(c in text for c in ["!", "💥", "🚨", "🔥", "😱", "💣"]):
            score += 2
        return round(score, 2)

    def _extract_location_tokens(self, text: str):
        words = re.findall(r"\b[A-ZÉÈÎÄÖÜ][a-zéèêàäöüß\-]{3,}\b", text)
        return [w for w in words if len(w) > 3]

    # ------------------------------------------------------------------
    def collect_recent_posts(self, limit=None):
        """Collect recent Bluesky posts safely (non-blocking)."""
        if time.time() - BlueskyCollector.last_rate_limit < self.cooldown_seconds:
            remaining = int(self.cooldown_seconds - (time.time() - BlueskyCollector.last_rate_limit))
            print(f"⏭️ Skipping Bluesky collection (cooldown {remaining}s left).")
            return []

        if not self.jwt_token:
            self._authenticate()
        if not self.jwt_token:
            print("⚠️ No valid Bluesky token — skipping fetch.")
            return []

        collected = []
        now = time.time()
        limit = limit or self.limit

        query = "attaque OR explosion OR fusillade OR verletzung OR bombe OR riot"
        params = {"q": query, "limit": limit}

        try:
            r = requests.get(
                f"{self.api_url}/xrpc/app.bsky.feed.searchPosts",
                headers=self._headers(),
                params=params,
                timeout=10,
            )
            if r.status_code == 429:
                print("⚠️ Bluesky rate limit hit during fetch — skipping for 5 minutes.")
                BlueskyCollector.last_rate_limit = time.time()
                return []
            r.raise_for_status()
            posts = r.json().get("posts", [])
        except Exception as e:
            print(f"⚠️ Bluesky fetch failed: {e}")
            return []

        for p in posts:
            record = p.get("record", {})
            text = self._clean_text(record.get("text", ""))
            if not text:
                continue

            score = self._compute_signal_score(text)
            if score < 5:
                continue

            tokens = self._extract_location_tokens(text)
            for t in tokens:
                self.recent_mentions[t].append(now)

            burst = any(
                len([t for t in ts if now - t < self.window_seconds]) >= 3
                for ts in self.recent_mentions.values()
            )
            if burst:
                score *= 1.5

            post_data = {
                "id": p.get("uri", ""),
                "platform": "bluesky",
                "language": self.language,
                "text": text,
                "timestamp": datetime.strptime(record.get("createdAt"), "%Y-%m-%dT%H:%M:%S.%fZ")
                .replace(tzinfo=timezone.utc)
                .timestamp(),
                "user": p.get("author", {}).get("handle", ""),
                "url": f"https://bsky.app/profile/{p.get('author', {}).get('handle', '')}/post/{p.get('uri', '').split('/')[-1]}",
                "media_attachments": [],
                "signal_score": score,
                "locations": [{"name": t, "city": t, "country": "unknown"} for t in tokens],
                "threat_classification": {
                    "risk_level": self._risk_level_from_score(score),
                    "primary_threat": self._guess_threat_type(text),
                    "urgency_detected": score >= 8,
                    "response_needed": "monitoring",
                },
            }

            collected.append(post_data)

        print(f"📡 Collected {len(collected)} Bluesky posts for lang={self.language}")
        return collected[:limit]

    # ------------------------------------------------------------------
    def _risk_level_from_score(self, score: float) -> str:
        if score >= 10:
            return "critical"
        elif score >= 7:
            return "high"
        elif score >= 4:
            return "medium"
        else:
            return "low"

    def _guess_threat_type(self, text: str) -> str:
        lang = self.language
        text_lower = text.lower()
        for category, data in THREAT_KEYWORDS.get(lang, {}).items():
            if any(k in text_lower for k in data["keywords"]):
                return category
        return "unknown"
