import time
import os
from dotenv import load_dotenv
from twitter_client import TwitterClient
from news_fetcher import NewsFetcher
from tweet_generator import TweetGenerator
from scheduler import Scheduler

load_dotenv()

def main():
    print("Starting X Market News Bot...")
    
    # Initialize components
    twitter = TwitterClient()
    news_fetcher = NewsFetcher()
    tweet_generator = TweetGenerator()
    scheduler = Scheduler(min_posts_per_day=int(os.getenv("POSTS_PER_DAY", 100)))
    
    # Optional: Initial dry run to see if it works
    print("Running initial news check...")
    news_items = news_fetcher.fetch_latest()
    impactful = news_fetcher.filter_market_impacting(news_items)
    
    if impactful:
        print(f"Found {len(impactful)} impactful news items.")
    else:
        print("No impactful news found in initial check.")

    while True:
        try:
            if scheduler.should_post():
                print("Checking for new news to post...")
                news_items = news_fetcher.fetch_latest()
                impactful = news_fetcher.filter_market_impacting(news_items)
                
                if impactful:
                    # Pick the most recent/impactful one
                    # For now, just pick the first one
                    news_to_post = impactful[0]
                    tweet_text = tweet_generator.format_tweet(news_to_post)
                    
                    if twitter.post_tweet(tweet_text):
                        scheduler.mark_posted()
                    else:
                        print("Failed to post tweet. Will try again in 5 minutes.")
                        time.sleep(300) # Wait 5 minutes before retry
                else:
                    print("No new impactful news found. Checking again in 15 minutes.")
                    time.sleep(900) # Wait 15 minutes
            else:
                # Sleep for a bit before checking scheduler again
                time.sleep(60) # Check every minute
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
