#!/usr/bin/env python3
"""
Test school and celebration venue detection
"""

import sys
sys.path.append('src')

from processing.location_extractor import LocationExtractor

def test_schools_events():
    print("🏫🎉 Testing School and Celebration Venue Detection")
    print("=" * 50)
    
    # Test French schools and events
    print("\n🇫🇷 French Schools & Events:")
    fr_extractor = LocationExtractor('fr')
    
    test_texts_fr = [
        "Fusillade dans un lycée à Paris",
        "Explosion pendant un concert au Bataclan",
        "Prise d'otages dans une école primaire",
        "Attaque au stade de France pendant un match",
        "Incident 14 juillet Champs-Élysées",
        "Alerte bombe au collège Samuel Paty"
    ]
    
    for text in test_texts_fr:
        locations = fr_extractor.extract_locations(text)
        print(f"\n📋 Text: {text}")
        for loc in locations:
            print(f"   📍 {loc['name']} - {loc['type']} - Risk: {loc['risk_level']}")
    
    # Test German schools and events
    print("\n🇩🇪 German Schools & Events:")
    de_extractor = LocationExtractor('de')
    
    test_texts_de = [
        "Amoklauf im Gymnasium Erfurt",
        "Explosion auf dem Weihnachtsmarkt Berlin",
        "Geiselnahme in der Grundschule",
        "Anschlag während Oktoberfest München",
        "Schießerei im Schulhof",
        "Bombe im Stadion während Bundesliga"
    ]
    
    for text in test_texts_de:
        locations = de_extractor.extract_locations(text)
        print(f"\n📋 Text: {text}")
        for loc in locations:
            print(f"   📍 {loc['name']} - {loc['type']} - Risk: {loc['risk_level']}")

if __name__ == "__main__":
    test_schools_events()