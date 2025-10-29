"""
Factory to switch between data collectors
"""

def get_collector(collector_type='mock', language='fr'):
    """
    Get a data collector based on type
    Options: 'mock', 'reddit', 'mastodon', 'bluesky', 'aggregated', 'simulation'
    """
    if collector_type == 'reddit':
        from .reddit_collector import RedditCollector
        return RedditCollector(language)

    elif collector_type == 'mastodon':
        from .mastodon_collector import MastodonCollector
        return MastodonCollector(language)

    elif collector_type == 'bluesky':
        from .bluesky_collector import BlueskyCollector
        return BlueskyCollector(language)

    elif collector_type == 'aggregated':
        from .aggregated_collector import AggregatedCollector
        return AggregatedCollector(language)

    elif collector_type == 'simulation':
        from .simulation_manager import SimulationManager
        return SimulationManager(language)

    else:
        from .threat_collector import ThreatCollector
        return ThreatCollector(language)
