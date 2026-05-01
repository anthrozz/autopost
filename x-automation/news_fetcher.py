import feedparser
import time

class NewsFetcher:
    FEEDS = [
        "https://www.cnbc.com/id/10000664/device/rss/rss.html", # Finance
        "https://www.cnbc.com/id/10001147/device/rss/rss.html", # Politics
        "https://finance.yahoo.com/news/rssindex",
        "https://www.marketwatch.com/site/rss",
        "https://www.investing.com/webmaster-tools/rss",
        "https://apnews.com/politics?utm_source=apnews.com&utm_medium=referral&utm_campaign=ap-rss&utm_term=rss"
    ]

    def __init__(self):
        self.seen_news = set()

    def fetch_latest(self):
        latest_news = []
        for url in self.FEEDS:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                if entry.link not in self.seen_news:
                    latest_news.append({
                        "title": entry.title,
                        "link": entry.link,
                        "summary": getattr(entry, "summary", ""),
                        "published": getattr(entry, "published", "")
                    })
                    # Keep track of seen news to avoid duplicates
                    self.seen_news.add(entry.link)
        
        # Sort by most recent if possible, or just return first few
        return latest_news

    def filter_market_impacting(self, news_items):
        # Basic filtering logic: look for keywords
        keywords = ["market", "stock", "inflation", "fed", "interest", "economy", "gdp", "trade", "election", "policy", "sanction", "war", "crisis"]
        impactful = []
        for item in news_items:
            content = (item["title"] + " " + item["summary"]).lower()
            if any(keyword in content for keyword in keywords):
                impactful.append(item)
        return impactful

if __name__ == "__main__":
    fetcher = NewsFetcher()
    news = fetcher.fetch_latest()
    print(f"Fetched {len(news)} items.")
    impactful = fetcher.filter_market_impacting(news)
    print(f"Impactful items: {len(impactful)}")
    for item in impactful[:3]:
        print(f"- {item['title']}")
