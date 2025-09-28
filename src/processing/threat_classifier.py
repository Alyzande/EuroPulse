"""
Automatically classify threats based on keywords and content
"""

import re
from src.data.threat_keywords import THREAT_KEYWORDS, URGENCY_INDICATORS

class ThreatClassifier:
    """Classify threats based on keyword analysis"""
    
    def __init__(self, language: str = 'fr'):
        self.language = language
        self.threat_keywords = THREAT_KEYWORDS[language]
        self.urgency_indicators = URGENCY_INDICATORS[language]
        print(f"🔍 Threat classifier initialized for {language}")
    
    def classify_threat(self, text: str) -> dict:
        """
        Analyze text and classify threat type, risk level, and response needed
        """
        text_lower = text.lower()
        classifications = []
        
        # Check each threat category
        for threat_type, threat_data in self.threat_keywords.items():
            keyword_matches = []
            
            for keyword in threat_data['keywords']:
                if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                    keyword_matches.append(keyword)
            
            if keyword_matches:
                classifications.append({
                    'threat_type': threat_type,
                    'risk_level': threat_data['risk_level'],
                    'response': threat_data['response'],
                    'keywords_found': keyword_matches,
                    'confidence': self._calculate_confidence(keyword_matches, threat_data['keywords'])
                })
        
        # Check for urgency indicators
        urgency_detected = any(indicator in text_lower for indicator in self.urgency_indicators)
        
        # Determine overall threat
        if classifications:
            primary_threat = max(classifications, key=lambda x: (x['confidence'], self._risk_weight(x['risk_level'])))
            
            return {
                'primary_threat': primary_threat['threat_type'],
                'risk_level': primary_threat['risk_level'],
                'response_needed': primary_threat['response'],
                'urgency_detected': urgency_detected,
                'all_detected_threats': [c['threat_type'] for c in classifications],
                'keywords_found': [keyword for c in classifications for keyword in c['keywords_found']],
                'confidence_score': primary_threat['confidence'],
                'classification_details': classifications
            }
        else:
            return {
                'primary_threat': 'unknown',
                'risk_level': 'low',
                'response_needed': 'monitoring',
                'urgency_detected': urgency_detected,
                'all_detected_threats': [],
                'keywords_found': [],
                'confidence_score': 0.0,
                'classification_details': []
            }
    
    def _calculate_confidence(self, found_keywords, all_keywords):
        """Calculate confidence based on keyword matches"""
        if not found_keywords:
            return 0.0
        return min(1.0, len(found_keywords) / len(all_keywords) * 2)  # Boost for partial matches
    
    def _risk_weight(self, risk_level):
        """Weight risk levels for prioritization"""
        weights = {'critical': 4, 'high': 3, 'medium': 2, 'low': 1}
        return weights.get(risk_level, 1)
    
    def get_threat_summary(self, posts):
        """Generate summary of threats across multiple posts"""
        threat_counts = {}
        high_risk_posts = []
        
        for post in posts:
            classification = self.classify_threat(post.get('clean_text', post.get('text', '')))
            
            if classification['primary_threat'] != 'unknown':
                threat_type = classification['primary_threat']
                threat_counts[threat_type] = threat_counts.get(threat_type, 0) + 1
                
                if classification['risk_level'] in ['high', 'critical']:
                    high_risk_posts.append({
                        'post': post,
                        'classification': classification
                    })
        
        return {
            'threat_breakdown': threat_counts,
            'high_risk_count': len(high_risk_posts),
            'total_threats_detected': sum(threat_counts.values()),
            'high_risk_posts': high_risk_posts
        }