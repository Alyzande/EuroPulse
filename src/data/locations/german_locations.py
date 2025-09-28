"""
High-risk locations for German-speaking countries and regions
"""

GERMAN_HIGH_RISK_LOCATIONS = [
    # 🇩🇪 GERMANY
    {'name': 'Breitscheidplatz', 'type': 'terrorist_attack_site', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'critical'},
    {'name': 'Kaiser-Wilhelm-Gedächtniskirche', 'type': 'terrorist_attack_site', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Alexanderplatz', 'type': 'terrorist_attack_site', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'high'},
    
   # 🏫 SCHOOLS (Under 18s)
    {'name': 'Gymnasium', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Realschule', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Grundschule', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Volksschule', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Schulhof', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Mensa', 'type': 'school', 'city': 'various', 'country': 'multiple', 'risk_level': 'medium'},
    
    # Specific school incidents
    {'name': 'Gutenberg-Gymnasium', 'type': 'school', 'city': 'Erfurt', 'country': 'Germany', 'risk_level': 'critical'},
    {'name': 'Albertville-Realschule', 'type': 'school', 'city': 'Winnenden', 'country': 'Germany', 'risk_level': 'critical'},
    
    # 🎉 CELEBRATION VENUES
    {'name': 'Breitscheidplatz', 'type': 'christmas_market', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'critical'},
    {'name': 'Olympiastadion', 'type': 'stadium', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Allianz Arena', 'type': 'stadium', 'city': 'München', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Signal Iduna Park', 'type': 'stadium', 'city': 'Dortmund', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Mercedes-Benz Arena', 'type': 'stadium', 'city': 'Stuttgart', 'country': 'Germany', 'risk_level': 'high'},
    
    # Concert venues
    {'name': 'Waldbühne', 'type': 'concert_venue', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'O2 World', 'type': 'concert_venue', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Philharmonie', 'type': 'concert_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': 'Festhalle', 'type': 'concert_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    
    # Festivals and events
    {'name': 'Oktoberfest', 'type': 'public_event', 'city': 'München', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Theresienwiese', 'type': 'public_event', 'city': 'München', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Weihnachtsmarkt', 'type': 'public_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'Karneval', 'type': 'public_event', 'city': 'Köln', 'country': 'Germany', 'risk_level': 'medium'},
    {'name': 'Fasching', 'type': 'public_event', 'city': 'München', 'country': 'Germany', 'risk_level': 'medium'},
    {'name': 'Feuerwerk', 'type': 'public_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    
    # Sports events
    {'name': 'Fußball', 'type': 'sports_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': 'Bundesliga', 'type': 'sports_event', 'city': 'multiple', 'country': 'Germany', 'risk_level': 'medium'},
    {'name': 'WM', 'type': 'sports_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'high'},
    {'name': 'EM', 'type': 'sports_event', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'high'},
    
    # 🎭 Cultural venues
    {'name': 'Konzerthaus', 'type': 'cultural_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': 'Staatsoper', 'type': 'cultural_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': 'Theater', 'type': 'cultural_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': 'Kino', 'type': 'cultural_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    {'name': 'Museum', 'type': 'cultural_venue', 'city': 'multiple', 'country': 'multiple', 'risk_level': 'medium'},
    
    # Austrian venues
    {'name': 'Ernst-Happel-Stadion', 'type': 'stadium', 'city': 'Wien', 'country': 'Austria', 'risk_level': 'high'},
    {'name': 'Wiener Stadthalle', 'type': 'concert_venue', 'city': 'Wien', 'country': 'Austria', 'risk_level': 'high'},
    
    # Swiss venues
    {'name': 'Stade de Suisse', 'type': 'stadium', 'city': 'Bern', 'country': 'Switzerland', 'risk_level': 'medium'},
    {'name': 'Hallestadion', 'type': 'concert_venue', 'city': 'Zürich', 'country': 'Switzerland', 'risk_level': 'medium'},

    # 🎄 Christmas Markets
    {'name': 'Christkindlesmarkt Nürnberg', 'type': 'christmas_market', 'city': 'Nürnberg', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Striezelmarkt Dresden', 'type': 'christmas_market', 'city': 'Dresden', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Weihnachtsmarkt Köln', 'type': 'christmas_market', 'city': 'Köln', 'country': 'Germany', 'risk_level': 'high'},
    
    # 🇦🇹 AUSTRIA
    {'name': 'Stephansplatz', 'type': 'terrorist_attack_site', 'city': 'Vienna', 'country': 'Austria', 'risk_level': 'high'},
    {'name': 'Schwedenplatz', 'type': 'terrorist_attack_site', 'city': 'Vienna', 'country': 'Austria', 'risk_level': 'high'},
    
    # 🇨🇭 SWITZERLAND
    {'name': 'Bahnhofstrasse', 'type': 'shopping_center', 'city': 'Zurich', 'country': 'Switzerland', 'risk_level': 'medium'},
    {'name': 'Bundeshaus', 'type': 'government_building', 'city': 'Bern', 'country': 'Switzerland', 'risk_level': 'medium'},
    
    # 🕌 Protest Locations
    {'name': 'Dresden', 'type': 'protest_site', 'city': 'Dresden', 'country': 'Germany', 'risk_level': 'medium'},
    {'name': 'PEGIDA', 'type': 'protest_site', 'city': 'Dresden', 'country': 'Germany', 'risk_level': 'medium'},
    {'name': 'Chemnitz', 'type': 'protest_site', 'city': 'Chemnitz', 'country': 'Germany', 'risk_level': 'medium'},
    
    # 🇮🇹 ITALY (South Tyrol)
    {'name': 'Piazza Walther', 'type': 'public_square', 'city': 'Bolzano', 'country': 'Italy', 'risk_level': 'low'},
    
    # 🇳🇦 NAMIBIA
    {'name': 'Alte Feste', 'type': 'museum', 'city': 'Windhoek', 'country': 'Namibia', 'risk_level': 'low'},
    
    # 🚇 Transportation Hubs
    {'name': 'Berlin Hauptbahnhof', 'type': 'transport_hub', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Hauptbahnhof Wien', 'type': 'transport_hub', 'city': 'Vienna', 'country': 'Austria', 'risk_level': 'high'},
    {'name': 'Flughafen BER', 'type': 'transport_hub', 'city': 'Berlin', 'country': 'Germany', 'risk_level': 'high'},
    {'name': 'Flughafen Zürich', 'type': 'transport_hub', 'city': 'Zurich', 'country': 'Switzerland', 'risk_level': 'high'}
]