import time
import random
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self, min_posts_per_day=20):
        self.min_posts_per_day = min_posts_per_day
        self.last_post_time = None
        self.next_post_time = self._calculate_next_post_time()

    def _calculate_next_post_time(self):
        # 24 hours / 5 posts = 4.8 hours average
        # Let's randomize between 2 hours and 6 hours
        wait_hours = random.uniform(0, 1)
        next_time = datetime.now() + timedelta(hours=wait_hours)
        print(f"Next post scheduled for: {next_time.strftime('%Y-%m-%d %H:%M:%S')}")
        return next_time

    def should_post(self):
        return datetime.now() >= self.next_post_time

    def mark_posted(self):
        self.last_post_time = datetime.now()
        self.next_post_time = self._calculate_next_post_time()

if __name__ == "__main__":
    scheduler = Scheduler()
    print(f"Should post now? {scheduler.should_post()}")
    print(f"Next post: {scheduler.next_post_time}")
