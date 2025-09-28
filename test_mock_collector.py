#!/usr/bin/env python3
"""
Test our mock collector - see immediate results!
"""

import sys
import os
sys.path.append('src')

from data.collectors.mock_collector import MockCollector

def test_collector():
    print("🧪 Testing Mock Collector")
    print("=" * 40)
    
    # Test French collector
    print("\n🇫🇷 Testing French posts:")
    fr_collector = MockCollector('fr')
    french_posts = fr_collector.collect_recent_posts(limit=5)
    
    for i, post in enumerate(french_posts):
        print(f"  {i+1}. {post['text']}")
        print(f"     Event: {post['event_type']}")
    
    # Test German collector  
    print("\n🇩🇪 Testing German posts:")
    de_collector = MockCollector('de')
    german_posts = de_collector.collect_recent_posts(limit=5)
    
    for i, post in enumerate(german_posts):
        print(f"  {i+1}. {post['text']}")
        print(f"     Event: {post['event_type']}")

if __name__ == "__main__":
    test_collector()