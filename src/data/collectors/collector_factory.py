"""
Factory to switch between mock data and real API collectors
"""

from .threat_collector import ThreatCollector

def get_collector(collector_type='mock', language='fr'):
    """
    Get a data collector based on type
    Options: 'mock', 'twitter', 'reddit'
    """
    if collector_type == 'twitter':
        # Import here to avoid circular imports
        from .twitter_collector import TwitterCollector
        return TwitterCollector(language)
    elif collector_type == 'reddit':
        # Import here to avoid circular imports  
        from .reddit_collector import RedditCollector
        return RedditCollector(language)
    else:
        # Fallback to threat collector (your working mock data)
        return ThreatCollector(language)