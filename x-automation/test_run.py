import os
from news_fetcher import NewsFetcher
from tweet_generator import TweetGenerator
from twitter_client import TwitterClient
from dotenv import load_dotenv
load_dotenv()
def test_components():
    print("--- Testing News Fetcher ---")
    fetcher = NewsFetcher()
    news = fetcher.fetch_latest()
    print(f"Fetched {len(news)} items.")
    
    impactful = fetcher.filter_market_impacting(news)
    print(f"Impactful items: {len(impactful)}")
    
    if impactful:
        print("\n--- Testing Tweet Generator ---")
        generator = TweetGenerator()
        tweet = generator.format_tweet(impactful[0])
        print(f"Generated Tweet: {tweet}")
        
        print("\n--- Testing Twitter Client (Dry Run) ---")
        os.environ["DRY_RUN"] = "True"
        client = TwitterClient()
        client.post_tweet(tweet)
    else:
        print("No impactful news found to test generator.")

if __name__ == "__main__":
    test_components()
