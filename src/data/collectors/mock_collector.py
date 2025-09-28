"""
Mock data collector for development and testing
Generates sample French and German social media posts about trending events
"""

import time
import random
from typing import List, Dict, Any


class MockCollector:
    """
    Simulates collecting social media posts in French or German
    Useful for development before setting up real API credentials
    """
    
    def __init__(self, language: str = 'fr'):
        self.language = language
        self.sample_events = self._get_sample_events(language)
        print(f"🎯 Mock collector initialized for {language} language")
    
    def collect_recent_posts(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Generate mock social media posts
        Returns: List of posts with text, language, timestamp, etc.
        """
        posts = []
        
        # Randomly pick 1-2 current events to simulate trending topics
        active_events = random.sample(self.sample_events, random.randint(1, 2))
        print(f"📊 Simulating events: {[e['name'] for e in active_events]}")
        
        for i in range(limit):
            # 70% chance post is about a trending event, 30% random noise
            if random.random() < 0.7:
                event = random.choice(active_events)
                post_text = random.choice(event['posts'])
                event_name = event['name']
            else:
                post_text = random.choice(self._get_random_posts(self.language))
                event_name = "random"
            
            post = {
                'id': f'mock_{int(time.time())}_{i}',
                'text': post_text,
                'language': self.language,
                'platform': 'mock',
                'timestamp': time.time() - random.randint(0, 3600),  # Last hour
                'user': f'user_{random.randint(1000, 9999)}',
                'event_type': event_name
            }
            
            posts.append(post)
        
        print(f"✅ Collected {len(posts)} mock posts in {self.language}")
        return posts
    
    def _get_sample_events(self, language: str) -> List[Dict]:
        """Sample trending events in French or German"""
        if language == 'fr':
            return [
                {
                    'name': 'Grève des transports',
                    'posts': [
                        "Grève des transports aujourd'hui, métro complètement arrêté #grève",
                        "Comment aller au travail avec cette grève? C'est impossible!",
                        "La grève des transports paralyse toute la ville ce matin",
                        "Solidarité avec les grévistes des transports en commun",
                        "Quand est-ce que cette grève va se terminer? Je suis bloqué"
                    ]
                },
                {
                    'name': 'Nouvelle loi environnement',
                    'posts': [
                        "La nouvelle loi sur l'environnement est enfin adoptée au parlement",
                        "Impact de la nouvelle loi environnement sur les entreprises locales",
                        "Cette loi environnement va changer beaucoup de choses pour le climat",
                        "Les écologistes satisfaits de la nouvelle législation verte"
                    ]
                }
            ]
        else:  # German
            return [
                {
                    'name': 'Verkehrsstreik',
                    'posts': [
                        "Verkehrsstreik heute, U-Bahn komplett eingestellt #streik",
                        "Wie komme ich zur Arbeit mit diesem Streik? Unmöglich!",
                        "Der Verkehrsstreik lähmt die gesamte Stadt heute Morgen",
                        "Solidarität mit den streikenden Verkehrsarbeitern",
                        "Wann endet dieser Streik endlich? Ich festsitzen"
                    ]
                },
                {
                    'name': 'Neues Umweltgesetz',
                    'posts': [
                        "Das neue Umweltgesetz wurde endlich verabschiedet im Parlament",
                        "Auswirkungen des neuen Umweltgesetzes auf Unternehmen vor Ort", 
                        "Dieses Umweltgesetz wird vieles verändern für das Klima",
                        "Umweltschützer zufrieden mit der neuen Gesetzgebung"
                    ]
                }
            ]
    
    def _get_random_posts(self, language: str) -> List[str]:
        """Random non-event posts (noise)"""
        if language == 'fr':
            return [
                "Beau temps aujourd'hui, parfait pour une promenade",
                "Quelqu'un a des recommandations de bons restaurants?",
                "Je viens de finir ce livre, il était incroyable!",
                "Quel film regarder ce weekend? Des suggestions?",
                "Le trafic est terrible en ce moment sur le périphérique"
            ]
        else:
            return [
                "Schönes Wetter heute, perfekt für einen Spaziergang",
                "Hat jemand Empfehlungen für gute Restaurants?",
                "Ich habe gerade dieses Buch beendet, es war unglaublich!",
                "Welchen Film soll ich dieses Wochenende schauen? Vorschläge?",
                "Der Verkehr ist momentan schrecklich auf der Ringstraße"
            ]