# src/data/collectors/twitter_collector.py
"""
Twitter/X API collector for real French and German threat detection
Focused on citizen reports and independent sources, NOT official news
"""

import os
import time
import random
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables at module level
load_dotenv()

try:
    import tweepy
    TWEEPY_AVAILABLE = True
except ImportError:
    TWEEPY_AVAILABLE = False
    print("⚠️ tweepy not installed - Twitter collector will use mock data")

class TwitterCollector:
    """Collects real tweets from regular users, NOT official news sources"""
    
    def __init__(self, language: str = 'fr'):
        self.language = language
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.client = None
        self.last_request_time = 0
        self.request_delay = 10  # 10 seconds between requests
        self.rate_limit_hit = False
        self.rate_limit_reset_time = 0
        
        # Blocklist of official/news accounts to EXCLUDE
        self.news_blocklist = [
            # French news
            'lemondefr', 'Le_Figaro', '20Minutes', 'franceinfo', 'BFMTV', 
            'LCI', 'Europe1', 'RTLFrance', 'France24_fr', 'FRANCE24',
            # German news
            'Tagesschau', 'ZEITonline', 'SPIEGEL_Politik', 'faznet', 'welt',
            'tazgezwitscher', 'DLF', 'ZDFheute', 'rtl_de', 'n_tv'
        ]
        
        if TWEEPY_AVAILABLE and self.bearer_token:
            try:
                self.client = tweepy.Client(bearer_token=self.bearer_token)
                print(f"✅ Twitter collector ready for {language} (excluding official news)")
            except Exception as e:
                print(f"❌ Twitter client setup failed: {e}")
                self.client = None
        else:
            if not TWEEPY_AVAILABLE:
                print("⚠️ tweepy not available - using mock data")
            if not self.bearer_token:
                print("⚠️ Twitter Bearer Token not found - using mock data")
        
    def collect_recent_posts(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Collect tweets from regular users about potential threats"""
        # If we recently hit rate limits, use mock data immediately
        if self.rate_limit_hit and time.time() < self.rate_limit_reset_time:
            remaining = int(self.rate_limit_reset_time - time.time())
            print(f"🔁 Still in rate limit cool-down ({remaining}s remaining), using mock data")
            return self._get_mock_tweets(limit)
        
        if not self.client:
            return self._get_mock_tweets(limit)
        
        try:
            # Rate limiting: wait if we made a request recently
            time_since_last_request = time.time() - self.last_request_time
            if time_since_last_request < self.request_delay:
                sleep_time = self.request_delay - time_since_last_request
                print(f"⏳ Rate limiting: waiting {sleep_time:.1f}s")
                time.sleep(sleep_time)
            
            # Try multiple targeted queries focused on citizen reports
            tweets = []
            queries = self._get_citizen_queries()
            
            for query in queries:
                if len(tweets) >= limit:
                    break
                    
                try:
                    self.last_request_time = time.time()
                    response = self.client.search_recent_tweets(
                        query=query,
                        max_results=min(8, limit - len(tweets)),  # Small batches
                        tweet_fields=['created_at', 'author_id', 'lang', 'public_metrics', 'context_annotations']
                    )
                    
                    if response.data:
                        for tweet in response.data:
                            # Skip if from news accounts
                            author_id = str(tweet.author_id)
                            
                            # Get user info to check if it's a news account
                            try:
                                user = self.client.get_user(id=author_id, user_fields=['username', 'description'])
                                username = user.data.username.lower() if user.data else ""
                                
                                # Skip if it's a known news account or sounds like news
                                if self._is_news_account(username, user.data.description if user.data else ""):
                                    continue
                                    
                            except:
                                # If we can't check user info, proceed but be cautious
                                pass
                            
                            tweet_data = {
                                'id': f'twitter_{tweet.id}',
                                'text': tweet.text,
                                'language': tweet.lang or self.language,
                                'platform': 'twitter',
                                'timestamp': tweet.created_at.timestamp() if tweet.created_at else None,
                                'user': f'user_{tweet.author_id}',
                                'query_used': query
                            }
                            tweets.append(tweet_data)
                                
                except Exception as e:
                    print(f"❌ Twitter query failed for '{query}': {e}")
                    continue
            
            # Return only the requested number of tweets
            tweets = tweets[:limit]
            
            if tweets:
                print(f"🐦 Collected {len(tweets)} citizen tweets in {self.language}")
                # Reset rate limit flag on successful request
                self.rate_limit_hit = False
            else:
                print(f"🔍 No citizen tweets found for {self.language}, using mock data")
                tweets = self._get_mock_tweets(limit)
                
            return tweets
            
        except tweepy.TooManyRequests as e:
            print("🚫 Twitter API rate limit hit - using mock data for 10 minutes")
            self.rate_limit_hit = True
            self.rate_limit_reset_time = time.time() + 600  # 10 minutes
            return self._get_mock_tweets(limit)
            
        except Exception as e:
            print(f"❌ Twitter API error: {e}")
            # Add extra delay on error to avoid hitting rate limits further
            time.sleep(5)
            return self._get_mock_tweets(limit)
    
    def _get_citizen_queries(self) -> List[str]:
        """Build search queries focused on citizen reports and eyewitness accounts"""
        if self.language == 'fr':
            return [
                # Citizen reports of emergencies
                "lang:fr (j'ai vu OR je viens de voir OR je viens d'entendre) (fusillade OR explosion OR coup de feu OR sirènes)",
                "lang:fr (police partout OR pompiers partout OR ambulance) -is:retweet -from:PoliceNationale -from:PompiersParis",
                "lang:fr (rue OR quartier OR centre-ville) (panique OR gens qui courent OR cris) -is:retweet",
                "lang:fr (entendu OR vu) (détonation OR explosion OR coup de feu) -is:retweet",
                "lang:fr (évacuez OR évacuation OR fuyez OR danger) -is:retweet"
            ]
        else:  # German
            return [
                # Citizen reports of emergencies
                "lang:de (habe gesehen OR gerade gesehen OR habe gehört) (schießerei OR explosion OR schüsse OR sirenen)",
                "lang:de (polizei überall OR feuerwehr überall OR krankenwagen) -is:retweet -from:PolizeiBerlin -from:Feuerwehr_Mu",
                "lang:de (straße OR viertel OR innenstadt) (panik OR leute rennen OR schreie) -is:retweet",
                "lang:de (gehört OR gesehen) (detonation OR explosion OR schüsse) -is:retweet",
                "lang:de (evakuiert OR evacuation OR flieht OR gefahr) -is:retweet"
            ]
    
    def _is_news_account(self, username: str, description: str) -> bool:
        """Check if an account is likely a news organization"""
        username_lower = username.lower()
        description_lower = description.lower()
        
        # Check against blocklist
        if any(news_account in username_lower for news_account in self.news_blocklist):
            return True
            
        # Check description for news indicators
        news_indicators = [
            'journalist', 'reporter', 'news', 'media', 'press', 'redaction',
            'journaliste', 'reporter', 'actualité', 'média', 'presse', 'rédaction',
            'journalist', 'reporter', 'nachrichten', 'medien', 'presse', 'redaktion'
        ]
        
        return any(indicator in description_lower for indicator in news_indicators)
    
    def _get_mock_tweets(self, limit: int) -> List[Dict[str, Any]]:
        """Fallback to mock data"""
        from .mock_collector import MockCollector
        mock = MockCollector(self.language)
        return mock.collect_recent_posts(limit)