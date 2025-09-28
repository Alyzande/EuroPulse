#!/usr/bin/env python3
"""
Test the location data files directly
"""

import sys
sys.path.append('src')

from data.locations.french_locations import FRENCH_HIGH_RISK_LOCATIONS
from data.locations.german_locations import GERMAN_HIGH_RISK_LOCATIONS
from data.locations.base_locations import HIGH_RISK_LOCATIONS

def test_location_data():
    print("📊 Testing Location Data Files")
    print("=" * 40)
    
    # Test French locations
    print(f"\n🇫🇷 French locations: {len(FRENCH_HIGH_RISK_LOCATIONS)} entries")
    countries_fr = set(loc['country'] for loc in FRENCH_HIGH_RISK_LOCATIONS)
    print(f"   Countries covered: {', '.join(countries_fr)}")
    
    # Count by country
    from collections import Counter
    country_counts = Counter(loc['country'] for loc in FRENCH_HIGH_RISK_LOCATIONS)
    for country, count in country_counts.most_common():
        risk_locs = [loc for loc in FRENCH_HIGH_RISK_LOCATIONS if loc['country'] == country and loc['risk_level'] in ['high', 'critical']]
        print(f"   {country}: {count} locations ({len(risk_locs)} high/critical risk)")
    
    # Test German locations
    print(f"\n🇩🇪 German locations: {len(GERMAN_HIGH_RISK_LOCATIONS)} entries")
    countries_de = set(loc['country'] for loc in GERMAN_HIGH_RISK_LOCATIONS)
    print(f"   Countries covered: {', '.join(countries_de)}")
    
    country_counts = Counter(loc['country'] for loc in GERMAN_HIGH_RISK_LOCATIONS)
    for country, count in country_counts.most_common():
        risk_locs = [loc for loc in GERMAN_HIGH_RISK_LOCATIONS if loc['country'] == country and loc['risk_level'] in ['high', 'critical']]
        print(f"   {country}: {count} locations ({len(risk_locs)} high/critical risk)")
    
    # Test base configuration
    print(f"\n🌍 Base configuration:")
    print(f"   French countries: {len(HIGH_RISK_LOCATIONS['fr']['countries'])}")
    print(f"   German countries: {len(HIGH_RISK_LOCATIONS['de']['countries'])}")

if __name__ == "__main__":
    test_location_data()