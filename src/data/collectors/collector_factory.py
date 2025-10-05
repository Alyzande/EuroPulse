"""
Factory to switch between data collectors
"""

def get_collector(collector_type='simulation', language='fr'):
    """
    Get a data collector based on type
    Options: 'mock', 'twitter', 'reddit', 'aggregated', 'simulation'
    """
    if collector_type == 'twitter':
        from .twitter_collector import TwitterCollector
        return TwitterCollector(language)
    elif collector_type == 'reddit':
        from .reddit_collector import RedditCollector
        return RedditCollector(language)
    elif collector_type == 'aggregated':
        from .aggregated_collector import AggregatedCollector
        return AggregatedCollector(language)
    elif collector_type == 'simulation':
        from .simulation_manager import SimulationManager
        return SimulationManager(language)
    else:
        from .threat_collector import ThreatCollector
        return ThreatCollector(language)