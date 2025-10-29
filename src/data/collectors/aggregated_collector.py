"""
Aggregates data from multiple sources (Reddit, Mastodon, Bluesky)
and normalizes platform information for each post.
"""

from typing import List, Dict, Any
from .reddit_collector import RedditCollector
from .mastodon_collector import MastodonCollector
from .bluesky_collector import BlueskyCollector
from .mock_collector import MockCollector


class AggregatedCollector:
    """Combines and normalizes threat intelligence data from multiple collectors."""

    def __init__(self, language: str = "fr"):
        self.language = language
        self.reddit_collector = RedditCollector(language)
        self.mastodon_collector = MastodonCollector(language)
        self.bluesky_collector = BlueskyCollector(language)
        print(f"🌍 AggregatedCollector initialized for language={language}")

    # ------------------------------------------------------------------
    def collect_recent_posts(self, limit: int = 30) -> List[Dict[str, Any]]:
        """Collect posts from all active sources and merge results."""

        all_posts: List[Dict[str, Any]] = []
        sources = {
            "reddit": self.reddit_collector,
            "mastodon": self.mastodon_collector,
            "bluesky": self.bluesky_collector,
        }

        for platform_name, collector in sources.items():
            try:
                posts = collector.collect_recent_posts(limit)
                if not posts:
                    print(f"ℹ️ {platform_name.capitalize()} returned 0 posts.")
                    continue

                for p in posts:
                    p["platform"] = p.get("platform", platform_name).lower().strip()
                    p["source_verified"] = True

                print(f"✅ {platform_name.capitalize()}: {len(posts)} posts")
                all_posts.extend(posts)

            except Exception as e:
                print(f"⚠️ {platform_name.capitalize()} failed: {e}")

        # ✅ NEW: return partial results even if one or more collectors failed
        if not all_posts:
            print("⚠️ No data collected — falling back to mock feed.")
            mock = MockCollector(self.language)
            all_posts = mock.collect_recent_posts(limit)
            for p in all_posts:
                p["platform"] = "mock"
                p["source_verified"] = False
        else:
            print(f"✅ Aggregator collected {len(all_posts)} total posts from working sources.")

        # Sort newest first
        all_posts.sort(key=lambda x: x.get("timestamp", 0), reverse=True)
        return all_posts
