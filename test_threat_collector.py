#!/usr/bin/env python3
"""
Test our threat detection system
"""

import sys
import os
sys.path.append('src')

from data.collectors.threat_collector import ThreatCollector

def test_threat_detection():
    print("🚨 Testing Threat Detection System")
    print("=" * 50)
    
    # Test French threat detection
    print("\n🇫🇷 French Threat Detection:")
    fr_threat = ThreatCollector('fr')
    french_posts = fr_threat.collect_recent_posts(limit=8)
    
    print("\nThreat Posts Found:")
    for i, post in enumerate(french_posts):
        if post['threat_level'] != 'normal':
            print(f"  🔥 {post['threat_type']} - {post['threat_level']} urgency")
            print(f"     {post['text']}")
    
    # Test German threat detection
    print("\n🇩🇪 German Threat Detection:")
    de_threat = ThreatCollector('de')  
    german_posts = de_threat.collect_recent_posts(limit=8)
    
    print("\nThreat Posts Found:")
    for i, post in enumerate(german_posts):
        if post['threat_level'] != 'normal':
            print(f"  🔥 {post['threat_type']} - {post['threat_level']} urgency")
            print(f"     {post['text']}")

if __name__ == "__main__":
    test_threat_detection()