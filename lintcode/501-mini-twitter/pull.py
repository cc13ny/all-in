'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
import heapq

class MiniTwitter:

    def __init__(self):
        # do intialization if necessary
        self.tweets = collections.defaultdict(list)
        self.followees = collections.defaultdict(set)
        self.time_count = 0
        self.tweet_limit = 10

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        self.time_count -= 1
        tweet = Tweet.create(user_id, tweet_text)
        self.tweets[user_id].insert(0, (self.time_count, tweet))
        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here

        def getInitialTweetHeap(user_id):
            heap = []
            user_list = [user_id] + list(self.followees[user_id])
            for i in range(len(user_list)):
                each_user_id = user_list[i]
                if each_user_id in self.tweets:
                    user_tweets = self.tweets[each_user_id]
                    if len(user_tweets) > 0:
                        heapq.heappush(heap, [user_tweets[0], 0])
            return heap

        def getTweetsWithLimitedNumber(heap, limit):
            res = []
            while len(heap) > 0 and len(res) < limit:
                (timestamp, tweet), idx = heapq.heappop(heap)

                user_tweets = self.tweets[tweet.user_id]
                if len(user_tweets) > idx + 1:
                    heapq.heappush(heap, [user_tweets[idx+1], idx+1])
                res.append(tweet)
            return res

        heap = getInitialTweetHeap(user_id)

        return getTweetsWithLimitedNumber(heap, self.tweet_limit)


    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        limit = self.tweet_limit
        return [tweet_pair[1] for tweet_pair in self.tweets[user_id][:limit]]

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        self.followees[from_user_id].add(to_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        self.followees[from_user_id].discard(to_user_id)