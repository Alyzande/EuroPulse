"""
Simulation manager for switching between real data and demo mode
"""

import os
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SimulationManager:
    """Manages switching between real data collection and simulation mode"""
    
    def __init__(self, language: str = 'fr'):
        self.language = language
        self.simulation_mode = os.getenv('SIMULATION_MODE', 'normal').lower() == 'simulation'
        
        # Import collectors (avoid circular imports)
        from .reddit_collector import RedditCollector
        from .twitter_collector import TwitterCollector
        from .threat_collector import ThreatCollector
        
        self.reddit_collector = RedditCollector(language)
        self.twitter_collector = TwitterCollector(language)
        self.threat_collector = ThreatCollector(language)
        
        mode = "🚨 SIMULATION" if self.simulation_mode else "📡 NORMAL"
        print(f"{mode} mode initialized for {language}")
    
    def set_simulation_mode(self, enabled: bool):
        """Toggle simulation mode"""
        self.simulation_mode = enabled
        mode = "🚨 SIMULATION" if enabled else "📡 NORMAL"
        print(f"🔄 Switched to {mode} mode")
        return enabled
    
    def collect_recent_posts(self, limit: int = 30) -> List[Dict[str, Any]]:
        """Collect data based on current mode"""
        if self.simulation_mode:
            print("🎭 Using simulated threat data for demonstration")
            return self.threat_collector.collect_recent_posts(limit)
        else:
            print("🌐 Collecting real data from Reddit and Twitter")
            # Use aggregated approach for real data
            reddit_limit = limit // 2
            twitter_limit = limit - reddit_limit
            
            reddit_posts = self.reddit_collector.collect_recent_posts(reddit_limit)
            twitter_posts = self.twitter_collector.collect_recent_posts(twitter_limit)
            
            combined = reddit_posts + twitter_posts
            print(f"📊 Real data: {len(reddit_posts)} Reddit + {len(twitter_posts)} Twitter posts")
            return combined
    
    def get_mode_status(self) -> Dict[str, Any]:
        """Return current mode status"""
        return {
            'simulation_mode': self.simulation_mode,
            'language': self.language,
            'description': 'Demonstration mode with threat scenarios' if self.simulation_mode else 'Real-time monitoring mode'
        }