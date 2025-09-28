"""
Threat keyword database for automatic classification
"""

THREAT_KEYWORDS = {
    'fr': {
        'shooting': {
            'keywords': ['fusillade', 'tir', 'coups de feu', 'kalachnikov', 'arme à feu', 'raffale', 'balles', 'mitraillette'],
            'risk_level': 'high',
            'response': 'SWAT, medical'
        },
        'explosion': {
            'keywords': ['explosion', 'détonation', 'bombe', 'engin explosif', 'dynamite', 'TATP', 'TNT', 'déflagration'],
            'risk_level': 'critical', 
            'response': 'bomb squad, evacuation'
        },
        'stabbing': {
            'keywords': ['couteau', 'poignard', 'arme blanche', 'taillade', 'égorgement', 'coup de couteau'],
            'risk_level': 'medium',
            'response': 'police, medical'
        },
        'vehicle_attack': {
            'keywords': ['camion bélier', 'véhicule fou', 'fonce dans la foule', 'attaque au véhicule', 'voiture piégée'],
            'risk_level': 'high',
            'response': 'barricades, traffic control'
        },
        'hostage': {
            'keywords': ['otage', 'prise d otages', 'séquestration', 'retenu contre son gré', 'geôlier'],
            'risk_level': 'high',
            'response': 'negotiation team, SWAT'
        },
        'riot': {
            'keywords': ['émeute', 'affrontement', 'casseur', 'barricade', 'projectile', 'CRS', 'manifestation violente','violences urbaines', 'casseurs', 'vitrines brisées', 'voitures incendiées', 'magasins pillés', 'affrontements violents','police-manifestants'],
            'risk_level': 'medium',
            'response': 'riot police, crowd control'
        },
        'school_threat': {
            'keywords': ['école', 'collège', 'lycée', 'cours de récréation', 'cantine scolaire', 'professeur agressé'],
            'risk_level': 'high',
            'response': 'school lockdown, child protection'
        },
        'public_event_threat': {
            'keywords': ['concert', 'stade', 'festival', 'feu d artifice', '14 juillet', 'foule compacte'],
            'risk_level': 'medium',
            'response': 'event security, evacuation'
        }
    },
    'de': {
        'shooting': {
            'keywords': ['schießerei', 'schüsse', 'gewehr', 'maschinenpistole', 'kugeln', 'feuerwaffe', 'schusswechsel'],
            'risk_level': 'high',
            'response': 'SEK, medical'
        },
        'explosion': {
            'keywords': ['explosion', 'detonation', 'bombe', 'sprengsatz', 'sprengstoff', 'dynamit', 'knall'],
            'risk_level': 'critical',
            'response': 'bomb squad, evacuation'
        },
        'stabbing': {
            'keywords': ['messer', 'messerangriff', 'stichwaffe', 'erstochen', 'messerstecherei', 'schnittverletzung'],
            'risk_level': 'medium',
            'response': 'police, medical'
        },
        'vehicle_attack': {
            'keywords': ['laster', 'fahrzeug', 'rast in menge', 'auto attacke', 'fahrzeugattentat', 'sprengstoffwagen', 'rammfahrzeug', 'auto rast', 'fußgängerzone'],
            'risk_level': 'high',
            'response': 'barricades, traffic control'
        },
        'hostage': {
            'keywords': ['geisel', 'geiselnahme', 'entführung', 'festgehalten', 'geiselnehmer'],
            'risk_level': 'high',
            'response': 'negotiation team, SEK'
        },
        'riot': {
            'keywords': ['krawall', 'ausschreitung', 'randalierer', 'barrikade', 'steinwurf', 'polizeieinsatz', 'zusammenstöße', 'demonstranten', 'projektile', 'eingeschlagene schaufenster'],
            'risk_level': 'medium',
            'response': 'riot police, crowd control'
        },
        'school_threat': {
            'keywords': ['schule', 'gymnasium', 'grundschule', 'schulhof', 'mensa', 'lehrer angegriffen'],
            'risk_level': 'high',
            'response': 'school lockdown, child protection'
        },
        'public_event_threat': {
            'keywords': ['konzert', 'stadion', 'fest', 'feuerwerk', 'oktoberfest', 'menschenmenge'],
            'risk_level': 'medium',
            'response': 'event security, evacuation'
        }
    }
}

URGENCY_INDICATORS = {
    'fr': ['maintenant', 'urgence', 'immédiat', 'panique', 'vite', 'secours', 'aide', 'sauvetage', 'cris'],
    'de': ['jetzt', 'sofort', 'notfall', 'panik', 'schnell', 'rettung', 'hilfe', 'notruf', 'schreie']
}