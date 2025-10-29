"""
Modular location extraction using separate data files
"""

import re
import os
from src.data.locations.french_locations import FRENCH_HIGH_RISK_LOCATIONS
from src.data.locations.german_locations import GERMAN_HIGH_RISK_LOCATIONS
from src.data.locations.base_locations import HIGH_RISK_LOCATIONS


class LocationExtractor:
    """Extract high-risk locations using modular data sources"""

    def __init__(self, language: str = 'fr'):
        self.language = language
        self.locations_db = self._load_locations_database(language)
        self.countries = HIGH_RISK_LOCATIONS[language]['countries']

        # Optional debug print
        self.debug = os.getenv("DEBUG_LOCATIONEXTRACTOR", "false").lower() == "true"
        if self.debug:
            print(f"🌍 Location extractor initialized for {language} - covering {len(self.countries)} countries (debug mode)")

    def _load_locations_database(self, language: str) -> list:
        """Load the appropriate location database"""
        if language == 'fr':
            return FRENCH_HIGH_RISK_LOCATIONS
        else:
            return GERMAN_HIGH_RISK_LOCATIONS

    def extract_locations(self, text: str) -> list:
        """Extract high-risk locations from text"""
        locations_found = []
        text_lower = text.lower()

        # Check database locations
        for location in self.locations_db:
            if location['name'].lower() in text_lower:
                locations_found.append(location)
                if self.debug:
                    print(f"📍 Found location: {location['name']}")

        # Check for country mentions
        for country in self.countries:
            if country.lower() in text_lower:
                locations_found.append({
                    'name': country,
                    'type': 'country',
                    'city': 'multiple',
                    'country': country,
                    'risk_level': 'medium'
                })
                if self.debug:
                    print(f"🌎 Country match detected: {country}")

        return locations_found

    def get_country_risk_profile(self, locations: list) -> dict:
        """Analyze which countries are mentioned and their risk levels"""
        country_risks = {}

        for location in locations:
            country = location.get('country', 'unknown')
            risk = location.get('risk_level', 'medium')

            if country not in country_risks:
                country_risks[country] = []

            country_risks[country].append({
                'location': location['name'],
                'risk': risk,
                'type': location['type']
            })

        return country_risks
