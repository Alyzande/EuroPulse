#!/usr/bin/env python3
"""
Test our threat detection system with modular locations and threat classification
"""

import sys
import os
sys.path.append('src')

from data.collectors.threat_collector import ThreatCollector

def test_threat_detection():
    print("🚨 Testing Threat Detection System with AI Classification")
    print("=" * 60)
    
    # Test French threat detection
    print("\n🇫🇷 French Threat Detection:")
    fr_threat = ThreatCollector('fr')
    french_posts = fr_threat.collect_recent_posts(limit=6)
    
    print("\nThreat Posts Found:")
    for i, post in enumerate(french_posts):
        if post['threat_level'] != 'normal':
            print(f"\n  🔥 POST {i+1}")
            print(f"     Text: {post['text']}")
            print(f"     Cleaned: {post.get('clean_text', 'N/A')}")
            
            # Show threat classification
            classification = post.get('threat_classification', {})
            if classification:
                print(f"     🎯 AI Classification: {classification.get('primary_threat', 'unknown')}")
                print(f"     🚨 Risk Level: {classification.get('risk_level', 'unknown')}")
                print(f"     🚑 Response: {classification.get('response_needed', 'unknown')}")
                print(f"     ⚡ Urgency: {classification.get('urgency_detected', False)}")
                print(f"     🔑 Keywords: {classification.get('keywords_found', [])}")
                print(f"     📊 Confidence: {classification.get('confidence_score', 0):.2f}")
            
            # Show locations
            if post.get('locations'):
                print(f"     📍 Locations: {len(post['locations'])} found")
                for loc in post['locations']:
                    print(f"        - {loc['name']} ({loc['country']}, {loc['city']}) - {loc['type']}")
            print("-" * 50)
    
    # Test German threat detection
    print("\n🇩🇪 German Threat Detection:")
    de_threat = ThreatCollector('de')  
    german_posts = de_threat.collect_recent_posts(limit=6)
    
    print("\nThreat Posts Found:")
    for i, post in enumerate(german_posts):
        if post['threat_level'] != 'normal':
            print(f"\n  🔥 POST {i+1}")
            print(f"     Text: {post['text']}")
            print(f"     Cleaned: {post.get('clean_text', 'N/A')}")
            
            # Show threat classification
            classification = post.get('threat_classification', {})
            if classification:
                print(f"     🎯 AI Classification: {classification.get('primary_threat', 'unknown')}")
                print(f"     🚨 Risk Level: {classification.get('risk_level', 'unknown')}")
                print(f"     🚑 Response: {classification.get('response_needed', 'unknown')}")
                print(f"     ⚡ Urgency: {classification.get('urgency_detected', False)}")
                print(f"     🔑 Keywords: {classification.get('keywords_found', [])}")
                print(f"     📊 Confidence: {classification.get('confidence_score', 0):.2f}")
            
            # Show locations
            if post.get('locations'):
                print(f"     📍 Locations: {len(post['locations'])} found")
                for loc in post['locations']:
                    print(f"        - {loc['name']} ({loc['country']}, {loc['city']}) - {loc['type']}")
            print("-" * 50)

if __name__ == "__main__":
    test_threat_detection()