import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

class TwitterClient:
    def __init__(self):
        self.api_key = os.getenv("X_API_KEY")
        self.api_secret = os.getenv("X_API_KEY_SECRET")
        self.access_token = os.getenv("X_ACCESS_TOKEN")
        self.access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
        self.bearer_token = os.getenv("X_BEARER_TOKEN")
        
        self.client = tweepy.Client(
            bearer_token=self.bearer_token,
            consumer_key=self.api_key,
            consumer_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )

    def post_tweet(self, text):
        if os.getenv("DRY_RUN") == "True":
            print(f"[DRY RUN] Would post: {text}")
            return True
        
        try:
            response = self.client.create_tweet(text=text)
            print(f"Successfully posted tweet! ID: {response.data['id']}")
            return True
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return False

if __name__ == "__main__":
    # Simple test
    client = TwitterClient()
    client.post_tweet("Testing my new market news bot! 📈🤖")
