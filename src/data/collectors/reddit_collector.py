"""
Reddit API collector for real French and German threat detection
Using read-only access (no authentication required)
"""

import praw
from typing import List, Dict, Any

class RedditCollector:
    """Collects real posts from Reddit using read-only access"""
    
    def __init__(self, language: str = 'fr'):
        self.language = language
        self.user_agent = 'EuroPulseThreatDetector/1.0'
        
        # Use a simple read-only Reddit instance
        self.reddit = praw.Reddit(
            client_id='KrDObbqXt4YWJBgirq0SNA',
            client_secret='9t_QtzjeOzrMj7dORV-tzJfmHnap6g', 
            user_agent=self.user_agent
        )
        
        self.subreddits = self._get_subreddits(language)
        print(f"✅ Reddit collector ready for {self.language}")
    
    def _get_subreddits(self, language: str) -> list:
        """Get relevant subreddits based on language"""
        if language == 'fr':
            return ['france', 'paris', 'lyon', 'actualite']  # Removed 'monde' (doesn't exist)
        else:  # German
            return ['de', 'berlin', 'germany', 'austria']    # Removed 'switzerland' (not active)
    
    def collect_recent_posts(self, limit: int = 25) -> List[Dict[str, Any]]:
        """Collect recent Reddit posts"""
        posts = []
        
        try:
            for subreddit_name in self.subreddits:
                try:
                    subreddit = self.reddit.subreddit(subreddit_name)
                    
                    # Get hot posts from the subreddit
                    for post in subreddit.hot(limit=8):
                        # Skip stickied posts (usually rules/megathreads)
                        if post.stickied:
                            continue
                            
                        post_data = {
                            'id': f'reddit_{post.id}',
                            'text': f"{post.title}. {post.selftext}" if post.selftext else post.title,
                            'language': self.language,
                            'platform': 'reddit',
                            'timestamp': post.created_utc,
                            'user': f'u/{post.author.name}' if post.author else 'unknown',
                            'url': f'https://reddit.com{post.permalink}',
                            'subreddit': subreddit_name
                            # Removed threat_type and threat_level - will be added by classification pipeline
                        }
                        posts.append(post_data)
                        
                        if len(posts) >= limit:
                            break
                            
                except Exception as e:
                    print(f"⚠️  Error from r/{subreddit_name}: {e}")
                    continue
                
                if len(posts) >= limit:
                    break
            
            # Debug: Show first 3 post titles
            if posts:
                print(f"🔍 Sample {self.language} Reddit posts:")
                for i, post in enumerate(posts[:3]):
                    print(f"   {i+1}. {post['text'][:100]}...")
            
            print(f"📡 Collected {len(posts)} real Reddit posts in {self.language}")
            return posts
            
        except Exception as e:
            print(f"❌ Error collecting Reddit posts: {e}")
            # Fallback to mock data
            from .threat_collector import ThreatCollector
            mock = ThreatCollector(self.language)
            return mock.collect_recent_posts(limit)