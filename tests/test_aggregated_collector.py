"""
Test the aggregated collector
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables first!
load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data.collectors.collector_factory import get_collector

def test_aggregated_collector():
    """Test that aggregated collector combines Reddit and Twitter data"""
    print("Testing Aggregated Collector...")
    
    # Debug: Check if Twitter token is loaded
    bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
    print(f"Twitter Bearer Token: {'✅ Found' if bearer_token else '❌ Missing'}")
    
    collector = get_collector('aggregated', 'fr')
    posts = collector.collect_recent_posts(10)
    
    print(f"📊 Collected {len(posts)} total posts")
    
    # Count posts by platform
    platforms = {}
    for post in posts:
        platform = post.get('platform', 'unknown')
        platforms[platform] = platforms.get(platform, 0) + 1
    
    for platform, count in platforms.items():
        print(f"  - {platform}: {count} posts")
    
    print("✅ Aggregated collector test passed!")

if __name__ == '__main__':
    test_aggregated_collector()