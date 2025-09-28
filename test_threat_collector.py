#!/usr/bin/env python3
"""
Test our threat detection system with modular locations
"""

import sys
import os
sys.path.append('src')

from data.collectors.threat_collector import ThreatCollector

def test_threat_detection():
    print("🚨 Testing Threat Detection System with Modular Locations")
    print("=" * 60)
    
    # Test French threat detection
    print("\n🇫🇷 French Threat Detection:")
    fr_threat = ThreatCollector('fr')
    french_posts = fr_threat.collect_recent_posts(limit=6)
    
    print("\nThreat Posts Found:")
    for i, post in enumerate(french_posts):
        if post['threat_level'] != 'normal':
            print(f"\n  🔥 {post['threat_type']} - {post['threat_level']} urgency")
            print(f"     Text: {post['text']}")
            if post.get('locations'):
                print(f"     📍 Locations: {[loc['name'] for loc in post['locations']]}")
                for loc in post['locations']:
                    print(f"        - {loc['name']} ({loc['country']}, {loc['city']}) - {loc['type']}")
    
    # Test German threat detection
    print("\n🇩🇪 German Threat Detection:")
    de_threat = ThreatCollector('de')  
    german_posts = de_threat.collect_recent_posts(limit=6)
    
    print("\nThreat Posts Found:")
    for i, post in enumerate(german_posts):
        if post['threat_level'] != 'normal':
            print(f"\n  🔥 {post['threat_type']} - {post['threat_level']} urgency")
            print(f"     Text: {post['text']}")
            if post.get('locations'):
                print(f"     📍 Locations: {[loc['name'] for loc in post['locations']]}")
                for loc in post['locations']:
                    print(f"        - {loc['name']} ({loc['country']}, {loc['city']}) - {loc['type']}")

if __name__ == "__main__":
    test_threat_detection()