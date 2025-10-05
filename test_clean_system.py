from src.data.collectors.collector_factory import get_collector

print("=== TESTING CLEAN SYSTEM (No Twitter) ===")
print("Testing aggregated collector...")
collector = get_collector('aggregated', 'fr')
posts = collector.collect_recent_posts(5)

print(f"âœ… Collected {len(posts)} posts")
for i, post in enumerate(posts):
    platform = post.get('platform', 'unknown')
    text = post['text'][:60] + '...' if len(post['text']) > 60 else post['text']
    print(f"{i+1}. [{platform}] {text}")

print("\ní¾‰ System is working without Twitter!")
