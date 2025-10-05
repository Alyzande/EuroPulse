"""
Aggregates data from multiple sources
"""

from typing import List, Dict, Any
from .reddit_collector import RedditCollector


class AggregatedCollector:
    """Combines data from multiple sources"""
    
    def __init__(self, language: str = 'fr'):
        self.language = language
        self.reddit_collector = RedditCollector(language)
        print(f"Aggregated collector initialized for {language}")
    
    def collect_recent_posts(self, limit: int = 30) -> List[Dict[str, Any]]:
        """Collect from available sources"""
        try:
            reddit_posts = self.reddit_collector.collect_recent_posts(limit)
            print(f"Aggregated {len(reddit_posts)} Reddit posts")
            return reddit_posts
        except Exception as e:
            print(f"Collection failed: {e}")
            from .mock_collector import MockCollector
            mock = MockCollector(self.language)
            return mock.collect_recent_posts(limit)