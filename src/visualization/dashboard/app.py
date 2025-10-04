#!/usr/bin/env python3
"""
EuroPulse Real-Time Threat Dashboard
"""

import sys
import os
import time
from flask import Flask, render_template, jsonify

# Add the root project directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.data.collectors.collector_factory import get_collector

app = Flask(__name__)

class Dashboard:
    def __init__(self):
        # Use environment variable to choose collector type, default to 'mock'
        collector_type = os.getenv('COLLECTOR_TYPE', 'mock')
        
        self.fr_collector = get_collector(collector_type, 'fr')
        self.de_collector = get_collector(collector_type, 'de')
        self.threat_history = []
        
        print(f"🌐 Using {collector_type} collectors for French and German")
    
    def _calculate_urgency(self, threat_level, text):
        """Calculate urgency based on threat level and content"""
        urgent_words = ['maintenant', 'urgence', 'immédiat', 'panique', 'aktuell', 'sofort', 'Notfall']
        text_lower = text.lower()
        
        if threat_level == 'critical':
            return 'critical'
        elif threat_level == 'high' and any(word in text_lower for word in urgent_words):
            return 'high'
        elif threat_level == 'high':
            return 'medium'
        else:
            return 'low'
    
    def get_current_threats(self):
        """Get current threats with prioritization"""
        try:
            fr_posts = self.fr_collector.collect_recent_posts(limit=8)
            de_posts = self.de_collector.collect_recent_posts(limit=8)
            
            all_posts = fr_posts + de_posts
            
            # Process posts through classification pipeline
            processed_posts = []
            for post in all_posts:
                # If it's a Reddit post, it needs classification
                if post.get('platform') == 'reddit' and 'threat_classification' not in post:
                    try:
                        # Import processors
                        from src.processing.text_cleaner import TextCleaner
                        from src.processing.threat_classifier import ThreatClassifier
                        from src.processing.location_extractor import LocationExtractor
                        
                        cleaner = TextCleaner(post['language'])
                        classifier = ThreatClassifier(post['language'])
                        location_extractor = LocationExtractor(post['language'])
                        
                        # Clean the text
                        post['clean_text'] = cleaner.clean_text(post['text'])
                        
                        # Classify the threat
                        post['threat_classification'] = classifier.classify_threat(post['text'])
                        
                        # Extract locations
                        post['locations'] = location_extractor.extract_locations(post['text'])
                        
                        # Set threat_level based on classification
                        classification = post['threat_classification']
                        post['threat_level'] = classification.get('risk_level', 'normal')
                        post['threat_type'] = classification.get('primary_threat', 'unknown')
                        
                        # Calculate urgency
                        post['urgency'] = self._calculate_urgency(post['threat_level'], post['text'])
                        
                    except Exception as e:
                        print(f"❌ Error processing Reddit post: {e}")
                        # Set defaults if processing fails
                        post['threat_level'] = 'normal'
                        post['threat_type'] = 'unknown'
                        post['urgency'] = 'low'
                        post['threat_classification'] = {}
                        post['locations'] = []
                        post['clean_text'] = post['text']
                
                processed_posts.append(post)
            
            threat_posts = [p for p in processed_posts if p['threat_level'] != 'normal']
            
            # Prioritize threats: critical > high > medium > low
            def threat_priority(post):
                classification = post.get('threat_classification', {})
                risk_level = classification.get('risk_level', 'low')
                urgency = classification.get('urgency_detected', False)
                
                # Priority weights
                weights = {'critical': 400, 'high': 300, 'medium': 200, 'low': 100}
                priority = weights.get(risk_level, 0)
                
                # Boost priority for urgent threats
                if urgency:
                    priority += 50
                    
                # Boost priority for recent threats (last 5 minutes)
                if post.get('timestamp', 0) > time.time() - 300:
                    priority += 25
                    
                return priority
            
            # Sort by priority (highest first)
            threat_posts.sort(key=threat_priority, reverse=True)
            
            # Add to history
            for post in threat_posts:
                self.threat_history.append({
                    'timestamp': time.time(),
                    'post': post,
                    'priority': threat_priority(post)
                })
            
            # Keep only last 50 threats
            self.threat_history = self.threat_history[-50:]
            
            return threat_posts
        except Exception as e:
            print(f"Error collecting threats: {e}")
            return []
    
    def get_threat_summary(self):
        """Get summary statistics"""
        threats = self.get_current_threats()
        
        if not threats:
            return {
                'total_threats': 0,
                'threat_types': {},
                'risk_levels': {'critical': 0, 'high': 0, 'medium': 0, 'low': 0},
                'countries': {},
                'languages': {'fr': 0, 'de': 0}
            }
        
        # Count statistics
        threat_types = {}
        risk_levels = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
        countries = {}
        languages = {'fr': 0, 'de': 0}
        
        for threat in threats:
            classification = threat.get('threat_classification', {})
            threat_type = classification.get('primary_threat', 'unknown')
            risk_level = classification.get('risk_level', 'low')
            
            threat_types[threat_type] = threat_types.get(threat_type, 0) + 1
            
            # Combine 'critical' and 'high' for statistics display
            actual_risk = 'high' if risk_level in ['high', 'critical'] else risk_level
            risk_levels[actual_risk] = risk_levels.get(actual_risk, 0) + 1
            
            languages[threat['language']] = languages.get(threat['language'], 0) + 1
            
            # Count countries from locations
            for location in threat.get('locations', []):
                country = location.get('country', 'unknown')
                countries[country] = countries.get(country, 0) + 1
        
        return {
            'total_threats': len(threats),
            'threat_types': threat_types,
            'risk_levels': risk_levels,
            'countries': countries,
            'languages': languages
        }

dashboard = Dashboard()

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/threats')
def get_threats():
    """API endpoint for current threats"""
    threats = dashboard.get_current_threats()
    return jsonify({
        'threats': threats,
        'total_threats': len(threats),
        'timestamp': time.time()
    })

@app.route('/api/stats')
def get_stats():
    """API endpoint for threat statistics"""
    stats = dashboard.get_threat_summary()
    return jsonify(stats)

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': time.time()})

if __name__ == '__main__':
    print("🚀 Starting EuroPulse Dashboard...")
    print("📊 Access at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)