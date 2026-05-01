import random

class TweetGenerator:
    def format_tweet(self, news_item):
        title = news_item["title"]
        # Basic templates to make it look professional
        templates = [
            "Market Update: {title} #Finance #Economy",
            "Key Insight: {title} What does this mean for the markets? 📊 #Trading",
            "Global Politics & Markets: {title} #Politics #Stocks",
            "Breaking: {title} Impacting financial decisions today. 📉📈",
            "Economic Alert: {title} Keep an eye on your portfolio. #Investing"
        ]
        
        template = random.choice(templates)
        tweet = template.format(title=title)
        
        # Ensure it fits within 280 characters
        if len(tweet) > 280:
            tweet = tweet[:277] + "..."
            
        return tweet

if __name__ == "__main__":
    generator = TweetGenerator()
    dummy_news = {"title": "Federal Reserve signals potential rate cut as inflation cools."}
    print(generator.format_tweet(dummy_news))
