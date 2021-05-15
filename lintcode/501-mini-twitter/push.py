'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
from bisect import bisect_left

class MiniTwitter:

    def __init__(self):
        # do intialization if necessary
        self.count_limit = 10
        self.time_stamp = 0
        self.followers = collections.defaultdict(set)
        self.news_feeds = collections.defaultdict(list)
        self.time_lines = collections.defaultdict(list)

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        self.time_stamp -= 1
        time_stamp = self.time_stamp

        tweet = Tweet.create(user_id, tweet_text)
        tweet_with_time_stamp = [time_stamp, tweet]

        self.news_feeds[user_id].insert(0, tweet_with_time_stamp)
        for follower_id in self.followers[user_id]:
            follower_news_feed = self.news_feeds[follower_id]
            idx = bisect_left(follower_news_feed, tweet_with_time_stamp)
            follower_news_feed.insert(idx, tweet_with_time_stamp)

        self.time_lines[user_id].insert(0, [time_stamp, tweet])
        return tweet


    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        return [tweet_with_time_stamp[1] for tweet_with_time_stamp in self.news_feeds[user_id][:self.count_limit]]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        return [tweet_with_time_stamp[1] for tweet_with_time_stamp in self.time_lines[user_id][:self.count_limit]]

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        self.followers[to_user_id].add(from_user_id)

        from_user_news_feed = self.news_feeds[from_user_id]
        to_user_time_line = self.time_lines[to_user_id]

        for tweet_with_time_stamp in to_user_time_line:
            idx = bisect_left(from_user_news_feed, tweet_with_time_stamp)
            from_user_news_feed.insert(idx, tweet_with_time_stamp)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        self.followers[to_user_id].discard(from_user_id)

        from_user_news_feed = self.news_feeds[from_user_id]
        to_user_time_line = self.time_lines[to_user_id]

        for tweet_with_time_stamp in to_user_time_line:
            time_stamp, tweet = tweet_with_time_stamp
            idx = bisect_left(from_user_news_feed, tweet_with_time_stamp)

            _, from_user_tweet = from_user_news_feed[idx]
            if from_user_tweet == tweet:
                from_user_news_feed.pop(idx)