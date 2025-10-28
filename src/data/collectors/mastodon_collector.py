#!/usr/bin/env python3
"""
Mastodon Collector - Weak Signal Detector
-----------------------------------------
Collects French and German posts from Mastodon public timelines,
applies lightweight weak-signal detection using THREAT_KEYWORDS
and URGENCY_INDICATORS to identify early signs of physical threats.

Outputs posts in the same schema as other collectors.
"""

import os
import time
import requests
import re
from collections import defaultdict, deque
from datetime import datetime, timezone
from urllib.parse import urljoin

from src.processing.threat_keywords import THREAT_KEYWORDS, URGENCY_INDICATORS


class MastodonCollector:
    """
    Weak-signal Mastodon collector that polls multiple instances
    for French and German posts and detects early threat signals.
    """

    def __init__(self, language="fr", limit=20):
        self.language = language
        self.limit = limit
        self.instances = [
            "https://mastodon.social",
            "https://mastodon.online",
            "https://mamot.fr",
            "https://piaille.fr",
            "https://mastodon.de",
            "https://chaos.social",
        ]
        self.token = os.getenv("MASTODON_ACCESS_TOKEN", "")
        self.headers = (
            {"Authorization": f"Bearer {self.token}"} if self.token else {}
        )

        # Rolling window for burst detection
        self.recent_mentions = defaultdict(lambda: deque(maxlen=50))
        self.window_seconds = 120  # 2-minute rolling window

        # Precompile regex for text cleaning
        self.clean_re = re.compile(r"<[^>]+>")

        print(f"✅ MastodonCollector initialized for language={language}")

    # ------------------------------------------------------------------
    # Internal utility methods
    # ------------------------------------------------------------------
    def _clean_html(self, text: str) -> str:
        return self.clean_re.sub("", text).replace("&quot;", '"').replace("&amp;", "&")

    def _get_recent_posts(self, instance_url):
        """Pull public timeline posts"""
        try:
            url = f"{instance_url}/api/v1/timelines/public?limit={self.limit}"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"⚠️ Mastodon fetch failed for {instance_url}: {e}")
            return []

    def _compute_signal_score(self, text: str) -> float:
        """Score post using THREAT_KEYWORDS and URGENCY_INDICATORS"""
        lang = self.language
        score = 0
        text_lower = text.lower()

        for category, data in THREAT_KEYWORDS.get(lang, {}).items():
            if any(k in text_lower for k in data["keywords"]):
                base = {
                    "low": 1,
                    "medium": 2,
                    "high": 3,
                    "critical": 4,
                }[data["risk_level"]]
                score += base

        if any(u in text_lower for u in URGENCY_INDICATORS.get(lang, [])):
            score *= 1.5

        # Add weight for exclamation / emojis
        if any(c in text for c in ["!", "💥", "🚨", "🔥", "😱", "💣"]):
            score += 2

        return round(score, 2)

    def _extract_location_tokens(self, text: str):
        """Extract capitalized words (possible locations)"""
        words = re.findall(r"\b[A-ZÉÈÎÄÖÜ][a-zéèêàäöüß\-]{3,}\b", text)
        return [w for w in words if len(w) > 3]

    # ------------------------------------------------------------------
    # Main logic
    # ------------------------------------------------------------------
    def collect_recent_posts(self, limit=None):
        """Collect and filter Mastodon posts"""
        collected = []
        now = time.time()
        limit = limit or self.limit

        for instance in self.instances:
            posts = self._get_recent_posts(instance)
            for p in posts:
                if not p.get("language") == self.language:
                    continue

                text = self._clean_html(p.get("content", ""))
                score = self._compute_signal_score(text)
                if score < 5:
                    continue  # too weak

                # Extract location-like tokens
                tokens = self._extract_location_tokens(text)
                for t in tokens:
                    self.recent_mentions[t].append(now)

                # Check burst rule
                burst = any(
                    len([t for t in ts if now - t < self.window_seconds]) >= 3
                    for ts in self.recent_mentions.values()
                )

                if burst:
                    score *= 1.5  # boost

                post_data = {
                    "id": p.get("id"),
                    "platform": "mastodon",
                    "language": self.language,
                    "text": text,
                    "timestamp": datetime.strptime(
                        p["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
                    )
                    .replace(tzinfo=timezone.utc)
                    .timestamp(),
                    "user": p.get("account", {}).get("acct", ""),
                    "url": p.get("url", ""),
                    "media_attachments": p.get("media_attachments", []),
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

            time.sleep(0.5)  # small delay between instances

        print(f"📡 Collected {len(collected)} Mastodon posts for lang={self.language}")
        return collected[:limit]

    # ------------------------------------------------------------------
    # Helpers for classification heuristics
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
