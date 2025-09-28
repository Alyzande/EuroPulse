"""
Threat-focused data collector
Simulates social media posts about physical danger events in French/German
"""

import time
import random
from typing import List, Dict, Any
from src.processing.text_cleaner import TextCleaner
from src.processing.location_extractor import LocationExtractor
from src.processing.threat_classifier import ThreatClassifier


class ThreatCollector:
    """
    Simulates collecting social media posts about physical threats
    Focused on events requiring police/emergency response
    """
    
    def __init__(self, language: str = 'fr'):
        self.language = language
        self.threat_events = self._get_threat_events(language)
        self.text_cleaner = TextCleaner(language)
        self.location_extractor = LocationExtractor(language)
        self.threat_classifier = ThreatClassifier(language)
        print(f"🚨 Threat collector initialized for {language} language")
    
    def collect_recent_posts(self, limit: int = 25) -> List[Dict[str, Any]]:
        """
        Generate mock posts about physical threats and emergencies
        """
        posts = []
        
        # Pick 1-2 active threat events
        active_threats = random.sample(self.threat_events, random.randint(1, 2))
        threat_names = [t['name'] for t in active_threats]
        print(f"🚨 Simulating threats: {threat_names}")
        
        for i in range(limit):
            # 80% chance post is about a threat, 20% normal posts (noise)
            if random.random() < 0.8:
                threat = random.choice(active_threats)
                post_text = random.choice(threat['posts'])
                threat_level = threat['level']
                threat_type = threat['name']
            else:
                post_text = random.choice(self._get_normal_posts(self.language))
                threat_level = "normal"
                threat_type = "daily_life"
            
            post = {
                'id': f'threat_{int(time.time())}_{i}',
                'text': post_text,
                'language': self.language,
                'platform': 'mock',
                'timestamp': time.time() - random.randint(0, 1800),  # Last 30 min
                'user': f'witness_{random.randint(1000, 9999)}',
                'threat_type': threat_type,
                'threat_level': threat_level,
                'urgency': self._calculate_urgency(threat_level, post_text)
            }
            post['clean_text'] = self.text_cleaner.clean_text(post_text)

                        # Extract locations from the original text
            post['locations'] = self.location_extractor.extract_locations(post_text)
            
            # Classify threat based on content
            post['threat_classification'] = self.threat_classifier.classify_threat(post_text)

            posts.append(post)
        
        print(f"📊 Collected {len(posts)} posts - {sum(1 for p in posts if p['threat_level'] != 'normal')} threat-related")
        return posts
    
    def _get_threat_events(self, language: str) -> List[Dict]:
        """Physical threat events requiring emergency response"""
        if language == 'fr':
            return [
                {
                    'name': 'Fusillade',
                    'level': 'high',
                    'posts': [
                        "Fusillade en cours près de la station République! Des coups de feu entendus",
                        "Tir actif dans le métro, police sur place, évitez le secteur",
                        "Attention fusillade centre-ville! Prenez refuge immédiatement",
                        "Coups de feu répétés rue de la Paix, situation confuse",
                        "Tirs entendus gare du Nord, panique générale #fusillade"
                    ]
                },
                {
                    'name': 'Attaque véhicule',
                    'level': 'high', 
                    'posts': [
                        "Camion fonce dans la foule sur les Champs-Élysées! Nombreux blessés",
                        "Véhicule bélier devant la préfecture, intention terroriste suspectée",
                        "Voiture folle dans zone piétonne, fuite du conducteur",
                        "Attaque au véhicule place Bellecour, cris et panique"
                    ]
                },
                {
                    'name': 'Explosion',
                    'level': 'critical',
                    'posts': [
                        "Grosse explosion entendue près aéroport CDG, fumée noire visible",
                        "Détonation centre commercial, vitres brisées, évacuation en cours",
                        "Explosion suspecte gare de Lyon, police et secours massifs",
                        "Bruit d'explosion rue de Rivoli, sirènes partout"
                    ]
                },
                {
                    'name': 'Agressions arme',
                    'level': 'medium',
                    'posts': [
                        "Homme armé d'un couteau dans le RER B, agressions multiples",
                        "Attaque au couteau marché aux puces, blessés graves",
                        "Individu armé fait irruption dans café, prise d'otages possible",
                        "Agressions en série avec arme blanche parc Montsouris"
                    ]
                },
                {
                    'name': 'Émeute',
                    'level': 'medium',
                    'posts': [
                        "Affrontements violents police-manifestants, projectiles lancés",
                        "Émeute en banlieue, voitures incendiées, magasins pillés",
                        "Violences urbaines quartier nord, barricades en feu",
                        "Groupe casseurs centre-ville, vitrines brisées"
                    ]
                }
            ]
        else:  # German
            return [
                {
                    'name': 'Schießerei',
                    'level': 'high',
                    'posts': [
                        "Schießerei am Hauptbahnhof! Schüsse gehört, Polizei im Einsatz",
                        "Aktiver Schütze in U-Bahn Station, Bereich absperren",
                        "Notfall: Schusswaffengebrauch Alexanderplatz, Menschen flüchten",
                        "Wiederholte Schüsse Friedrichstraße, Situation unklar",
                        "Kugeln gehört am Ku'damm, allgemeine Panik #Schießerei"
                    ]
                },
                {
                    'name': 'Fahrzeugangriff',
                    'level': 'high',
                    'posts': [
                        "Laster rast in Menschenmenge am Brandenburger Tor! Viele Verletzte",
                        "Rammfahrzeug vor Rathaus, mutmaßlich terroristischer Hintergrund",
                        "Auto rast durch Fußgängerzone, Fahrer flüchtig",
                        "Fahrzeugattacke Marienplatz, Schreie und Panik"
                    ]
                },
                {
                    'name': 'Explosion',
                    'level': 'critical',
                    'posts': [
                        "Starke Explosion nahe Flughafen BER, schwarzer Rauch sichtbar",
                        "Detonation Einkaufszentrum, zerbrochene Fenster, Evakuierung läuft",
                        "Verdächtige Explosion Hauptbahnhof, massive Polizei- und Rettungskräfte",
                        "Explosionsgeräusch Unter den Linden, Sirenen überall"
                    ]
                },
                {
                    'name': 'Messerangriffe',
                    'level': 'medium',
                    'posts': [
                        "Mann mit Messer in S-Bahn, mehrere Angriffe gemeldet",
                        "Messerattacke Flohmarkt, schwer verletzte Opfer",
                        "Bewaffneter Eindringling in Café, mögliche Geiselnahme",
                        "Serienangriffe mit Messer im Tiergarten Park"
                    ]
                },
                {
                    'name': 'Krawalle',
                    'level': 'medium',
                    'posts': [
                        "Zusammenstöße Polizei-Demonstranten, Projektile geworfen",
                        "Krawalle Vorstadt, brennende Autos, geplünderte Geschäfte",
                        "Urbane Gewalt Nordviertel, brennende Barrikaden",
                        "Randalierer Innenstadt, eingeschlagene Schaufenster"
                    ]
                }
            ]
    
    def _get_normal_posts(self, language: str) -> List[str]:
        """Normal daily posts (noise)"""
        if language == 'fr':
            return [
                "Beau temps pour une balade aujourd'hui",
                "Quelqu'un a testé le nouveau restaurant italien?",
                "Trafic normal sur le périphérique ce matin",
                "Concert sympa hier soir, bonne ambiance"
            ]
        else:
            return [
                "Schönes Wetter für einen Spaziergang heute",
                "Hat jemand das neue italienische Restaurant probiert?",
                "Normaler Verkehr auf dem Ring heute Morgen",
                "Gutes Konzert gestern Abend, tolle Stimmung"
            ]
    
    def _calculate_urgency(self, threat_level: str, text: str) -> str:
        """Calculate urgency based on threat level and content"""
        urgent_words = ['maintenant', 'urgence', 'panique', 'immédiat', 'aktuell', 'sofort', 'Notfall']
        if threat_level == 'critical':
            return 'critical'
        elif threat_level == 'high' and any(word in text.lower() for word in urgent_words):
            return 'high'
        elif threat_level == 'high':
            return 'medium'
        else:
            return 'low'