#!/usr/bin/env python3
"""
Test the modular location extraction system
"""

import sys
sys.path.append('src')

from processing.location_extractor import LocationExtractor

def test_modular_extraction():
    print("🌍 Testing Modular Location Extraction")
    print("=" * 50)
    
    # Test French locations across multiple countries
    print("\n🇫🇷 French-speaking countries coverage:")
    fr_extractor = LocationExtractor('fr')
    
    test_texts_fr = [
        "Explosion près du Bataclan à Paris",  # France
        "Attaque à la gare de Maelbeek Bruxelles",  # Belgium
        "Prise d'otages Radisson Blu Bamako",  # Mali
        "Fusillade Grand-Bassam Côte d'Ivoire",  # Ivory Coast
        "Incident au Parlement Européen Bruxelles"  # International org
    ]
    
    for text in test_texts_fr:
        locations = fr_extractor.extract_locations(text)
        print(f"\n📋 Text: {text}")
        print(f"📍 Locations found: {len(locations)}")
        for loc in locations:
            print(f"   → {loc['name']} ({loc['country']}) - {loc['type']} - Risk: {loc['risk_level']}")
    
    # Test German locations across multiple countries
    print("\n🇩🇪 German-speaking countries coverage:")
    de_extractor = LocationExtractor('de')
    
    test_texts_de = [
        "Anschlag Breitscheidplatz Berlin",  # Germany
        "Explosion Stephansplatz Wien",  # Austria
        "Proteste PEGIDA Dresden",  # Germany protests
        "Incident Bahnhofstrasse Zürich",  # Switzerland
        "Unruhen Chemnitz"  # Germany protests
    ]
    
    for text in test_texts_de:
        locations = de_extractor.extract_locations(text)
        print(f"\n📋 Text: {text}")
        print(f"📍 Locations found: {len(locations)}")
        for loc in locations:
            print(f"   → {loc['name']} ({loc['country']}) - {loc['type']} - Risk: {loc['risk_level']}")
    
    # Test country risk profiling
    print("\n🎯 Country Risk Analysis:")
    sample_locations = [
        {'name': 'Bataclan', 'type': 'terrorist_attack_site', 'city': 'Paris', 'country': 'France', 'risk_level': 'critical'},
        {'name': 'Maelbeek', 'type': 'terrorist_attack_site', 'city': 'Brussels', 'country': 'Belgium', 'risk_level': 'high'},
        {'name': 'Radisson Blu', 'type': 'terrorist_attack_site', 'city': 'Bamako', 'country': 'Mali', 'risk_level': 'critical'}
    ]
    
    country_risks = fr_extractor.get_country_risk_profile(sample_locations)
    for country, risks in country_risks.items():
        print(f"   {country}: {len(risks)} high-risk locations")
        for risk in risks:
            print(f"     - {risk['location']}: {risk['risk']} risk")

if __name__ == "__main__":
    test_modular_extraction()