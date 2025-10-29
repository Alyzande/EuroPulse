"""
Aggregates data from multiple sources
"""

from typing import List, Dict, Any
from .reddit_collector import RedditCollector
from .mastodon_collector import MastodonCollector
from .bluesky_collector import BlueskyCollector
from .mock_collector import MockCollector


class AggregatedCollector:
    """Combines data from multiple real sources"""

    def __init__(self, language: str = 'fr'):
        self.language = language
        self.reddit_collector = RedditCollector(language)
        self.mastodon_collector = MastodonCollector(language)
        self.bluesky_collector = BlueskyCollector(language)
        print(f"🌍 AggregatedCollector initialized for language={language}")

    def collect_recent_posts(self, limit: int = 30) -> List[Dict[str, Any]]:
        """Collect from all available sources and merge them"""

        all_posts = []

        # Try Reddit
        try:
            reddit_posts = self.reddit_collector.collect_recent_posts(limit)
            for p in reddit_posts:
                p["platform"] = p.get("platform", "reddit")
            print(f"✅ Reddit: {len(reddit_posts)} posts")
            all_posts.extend(reddit_posts)
        except Exception as e:
            print(f"⚠️ Reddit failed: {e}")

        # Try Mastodon
        try:
            mastodon_posts = self.mastodon_collector.collect_recent_posts(limit)
            for p in mastodon_posts:
                p["platform"] = p.get("platform", "mastodon")
            print(f"✅ Mastodon: {len(mastodon_posts)} posts")
            all_posts.extend(mastodon_posts)
        except Exception as e:
            print(f"⚠️ Mastodon failed: {e}")

        # Try Bluesky
        try:
            bluesky_posts = self.bluesky_collector.collect_recent_posts(limit)
            for p in bluesky_posts:
                p["platform"] = p.get("platform", "bluesky")
            print(f"✅ Bluesky: {len(bluesky_posts)} posts")
            all_posts.extend(bluesky_posts)
        except Exception as e:
            print(f"⚠️ Bluesky failed: {e}")

        # Fallback if nothing fetched
        if not all_posts:
            print("⚠️ No data collected — falling back to mock.")
            mock = MockCollector(self.language)
            all_posts = mock.collect_recent_posts(limit)
            for p in all_posts:
                p["platform"] = "mock"

        # Optional: sort by timestamp (newest first)
        all_posts.sort(key=lambda x: x.get("timestamp", 0), reverse=True)

        print(f"🧩 Aggregated total: {len(all_posts)} posts from multiple sources.")
        return all_posts
