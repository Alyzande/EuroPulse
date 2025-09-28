"""
Base location data structure for threat intelligence
"""

HIGH_RISK_LOCATIONS = {
    'fr': {
        'countries': ['France', 'Belgium', 'Switzerland', 'Luxembourg', 'Mali', 'Burkina Faso', 'Niger', 'Chad', 'DR Congo', 'Ivory Coast'],
        
        # Location types with risk weights
        'location_types': {
            'christmas_market': 0.9,
            'terrorist_attack_site': 1.0,
            'government_building': 0.8,
            'religious_site': 0.7,
            'transport_hub': 0.8,
            'shopping_center': 0.6,
            'hotel': 0.7,
            'protest_site': 0.5,
            'international_org': 0.9
        }
    },
    'de': {
        'countries': ['Germany', 'Austria', 'Switzerland', 'Liechtenstein', 'Belgium', 'Italy', 'Namibia'],
        
        'location_types': {
            'christmas_market': 0.9,
            'terrorist_attack_site': 1.0,
            'government_building': 0.8,
            'religious_site': 0.7,
            'transport_hub': 0.8,
            'shopping_center': 0.6,
            'hotel': 0.7,
            'protest_site': 0.5,
            'international_org': 0.9
        }
    }
}