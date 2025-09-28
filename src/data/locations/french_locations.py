"""
High-risk locations for French-speaking countries and regions
"""

FRENCH_HIGH_RISK_LOCATIONS = [
    # 🇫🇷 FRANCE
    {'name': 'Bataclan', 'type': 'terrorist_attack_site', 'city': 'Paris', 'country': 'France', 'risk_level': 'critical'},
    {'name': 'Stade de France', 'type': 'terrorist_attack_site', 'city': 'Paris', 'country': 'France', 'risk_level': 'critical'},
    {'name': 'Promenade des Anglais', 'type': 'terrorist_attack_site', 'city': 'Nice', 'country': 'France', 'risk_level': 'critical'},
    {'name': 'Hyper Cacher', 'type': 'terrorist_attack_site', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    

    # 🏫 SCHOOLS (Under 18s)
    {'name': 'Lycée', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Collège', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'École primaire', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'École maternelle', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Cours de récréation', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Cantine scolaire', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'medium'},
    
    # Specific high-profile school incidents
    {'name': 'Lycée Samuel Paty', 'type': 'school', 'city': 'Conflans-Sainte-Honorine', 'country': 'France', 'risk_level': 'critical'},
    {'name': 'Collège du Bois d\'Aulne', 'type': 'school', 'city': 'Conflans-Sainte-Honorine', 'country': 'France', 'risk_level': 'high'},
    
    # 🎉 CELEBRATION VENUES
    {'name': 'Bataclan', 'type': 'concert_venue', 'city': 'Paris', 'country': 'France', 'risk_level': 'critical'},
    {'name': 'Stade de France', 'type': 'stadium', 'city': 'Paris', 'country': 'France', 'risk_level': 'critical'},
    {'name': 'Stade Vélodrome', 'type': 'stadium', 'city': 'Marseille', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Parc des Princes', 'type': 'stadium', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Stade Gerland', 'type': 'stadium', 'city': 'Lyon', 'country': 'France', 'risk_level': 'high'},
    
    # Concert venues
    {'name': 'Olympia', 'type': 'concert_venue', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    {'name': 'AccorHotels Arena', 'type': 'concert_venue', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Zénith', 'type': 'concert_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': 'Bercy', 'type': 'concert_venue', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    
    # Festivals and events
    {'name': 'Fête de la Musique', 'type': 'public_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': '14 juillet', 'type': 'national_celebration', 'city': 'multiple', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Bastille Day', 'type': 'national_celebration', 'city': 'multiple', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Feu d\'artifice', 'type': 'public_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    
    # Sports events
    {'name': 'Coupe du Monde', 'type': 'sports_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Euro', 'type': 'sports_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Tour de France', 'type': 'sports_event', 'city': 'multiple', 'country': 'France', 'risk_level': 'medium'},
    {'name': 'Roland Garros', 'type': 'sports_event', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    
    # 🎭 Cultural venues
    {'name': 'Opéra Garnier', 'type': 'cultural_venue', 'city': 'Paris', 'country': 'France', 'risk_level': 'medium'},
    {'name': 'Opéra Bastille', 'type': 'cultural_venue', 'city': 'Paris', 'country': 'France', 'risk_level': 'medium'},
    {'name': 'Théâtre', 'type': 'cultural_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': 'Cinéma', 'type': 'cultural_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},


    # 🎄 Christmas Markets
    {'name': 'Marché de Noël Strasbourg', 'type': 'christmas_market', 'city': 'Strasbourg', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Marché de Noël Colmar', 'type': 'christmas_market', 'city': 'Colmar', 'country': 'France', 'risk_level': 'high'},
    
    # 🇧🇪 BELGIUM
    {'name': 'Grand Place', 'type': 'terrorist_attack_site', 'city': 'Brussels', 'country': 'Belgium', 'risk_level': 'high'},
    {'name': 'Maelbeek', 'type': 'terrorist_attack_site', 'city': 'Brussels', 'country': 'Belgium', 'risk_level': 'high'},
    {'name': 'Zaventem', 'type': 'terrorist_attack_site', 'city': 'Brussels', 'country': 'Belgium', 'risk_level': 'high'},
    
    # 🇨🇭 SWITZERLAND
    {'name': 'Rigigen', 'type': 'protest_site', 'city': 'Bern', 'country': 'Switzerland', 'risk_level': 'medium'},
    
    # 🇲🇱 MALI (Sahel Region - High Threat)
    {'name': 'Radisson Blu', 'type': 'terrorist_attack_site', 'city': 'Bamako', 'country': 'Mali', 'risk_level': 'critical'},
    {'name': 'Hotel Byblos', 'type': 'terrorist_attack_site', 'city': 'Sévaré', 'country': 'Mali', 'risk_level': 'high'},
    
    # 🇧🇫 BURKINA FASO
    {'name': 'Cappuccino Café', 'type': 'terrorist_attack_site', 'city': 'Ouagadougou', 'country': 'Burkina Faso', 'risk_level': 'high'},
    {'name': 'Splendid Hotel', 'type': 'terrorist_attack_site', 'city': 'Ouagadougou', 'country': 'Burkina Faso', 'risk_level': 'high'},
    
    # 🇨🇮 IVORY COAST
    {'name': 'Grand-Bassam', 'type': 'terrorist_attack_site', 'city': 'Grand-Bassam', 'country': 'Ivory Coast', 'risk_level': 'high'},
    
    # 🏛️ International Organizations
    {'name': 'Parlement Européen', 'type': 'international_org', 'city': 'Brussels', 'country': 'Belgium', 'risk_level': 'high'},
    {'name': 'NATO', 'type': 'international_org', 'city': 'Brussels', 'country': 'Belgium', 'risk_level': 'high'},
    {'name': 'ONU', 'type': 'international_org', 'city': 'Geneva', 'country': 'Switzerland', 'risk_level': 'high'},
    
    # 🚇 Transportation Hubs (Multiple Countries)
    {'name': 'Gare du Nord', 'type': 'transport_hub', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Gare de Lyon', 'type': 'transport_hub', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Aéroport CDG', 'type': 'transport_hub', 'city': 'Paris', 'country': 'France', 'risk_level': 'high'},
    {'name': 'Aéroport de Zaventem', 'type': 'transport_hub', 'city': 'Brussels', 'country': 'Belgium', 'risk_level': 'high'}
]