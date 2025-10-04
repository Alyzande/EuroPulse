#!/usr/bin/env python3
"""
Test automatic threat classification
"""

import sys
sys.path.append('src')

from processing.threat_classifier import ThreatClassifier

def test_threat_classification():
    print("🔍 Testing Threat Classification System")
    print("=" * 50)
    
    # Test French threat classification
    print("\n🇫🇷 French Threat Classification:")
    fr_classifier = ThreatClassifier('fr')
    
    test_texts_fr = [
        "Fusillade en cours près de la gare, coups de feu entendus URGENCE",
        "Explosion suspecte dans le métro, possible bombe",
        "Homme avec un couteau devant le lycée, élèves en danger",
        "Camion fou fonce dans la foule sur les Champs-Élysées",
        "Prise d'otages dans une banque, situation critique",
        "Émeute en centre-ville, casseurs et projectiles"
    ]
    
    for text in test_texts_fr:
        classification = fr_classifier.classify_threat(text)
        print(f"\n📋 Text: {text}")
        print(f"   🎯 Primary threat: {classification['primary_threat']}")
        print(f"   🚨 Risk level: {classification['risk_level']}")
        print(f"   🚑 Response: {classification['response_needed']}")
        print(f"   ⚡ Urgency: {classification['urgency_detected']}")
        print(f"   🔑 Keywords: {classification['keywords_found']}")
        print(f"   📊 Confidence: {classification['confidence_score']:.2f}")
    
    # Test German threat classification
    print("\n🇩🇪 German Threat Classification:")
    de_classifier = ThreatClassifier('de')
    
    test_texts_de = [
        "Schießerei am Hauptbahnhof! Schüsse gehört SOFORT",
        "Explosion im Kaufhaus, möglicher Sprengsatz",
        "Messerangriff in der Schule, Kinder in Gefahr",
        "Laster rast in Menschenmenge am Brandenburger Tor",
        "Geiselnahme im Supermarkt, kritische Situation",
        "Krawalle in der Innenstadt, Randalierer werfen Steine"
    ]
    
    for text in test_texts_de:
        classification = de_classifier.classify_threat(text)
        print(f"\n📋 Text: {text}")
        print(f"   🎯 Primary threat: {classification['primary_threat']}")
        print(f"   🚨 Risk level: {classification['risk_level']}")
        print(f"   🚑 Response: {classification['response_needed']}")
        print(f"   ⚡ Urgency: {classification['urgency_detected']}")
        print(f"   🔑 Keywords: {classification['keywords_found']}")
        print(f"   📊 Confidence: {classification['confidence_score']:.2f}")

if __name__ == "__main__":
    test_threat_classification()