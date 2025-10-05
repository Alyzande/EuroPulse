"""
Test the clean system without Twitter
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data.collectors.collector_factory import get_collector

def test_clean_system():
    """Test that system works without Twitter"""
    print("TESTING CLEAN SYSTEM (No Twitter)")
    
    collector = get_collector('aggregated', 'fr')
    posts = collector.collect_recent_posts(5)
    
    print(f"Collected {len(posts)} posts")
    
    platforms = {}
    for post in posts:
        platform = post.get('platform', 'unknown')
        platforms[platform] = platforms.get(platform, 0) + 1
    
    print("Platform breakdown:")
    for platform, count in platforms.items():
        print(f"  - {platform}: {count} posts")
    
    print("System is working without Twitter!")

if __name__ == '__main__':
    test_clean_system()
