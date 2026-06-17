class Twitter:

    def __init__(self):
        self.count = 0
        self.following = defaultdict(set) # userId -> set of ids
        self.tweets = defaultdict(list) # userId -> list of tweets in ORDER

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        feed = []

        self.following[userId].add(userId)
        # get most recent tweets for each following
        for following in self.following[userId]:
            if following in self.tweets:
                i = len(self.tweets[following]) - 1
                count, tweetId = self.tweets[following][i]
                heapq.heappush(maxHeap, [count, tweetId, following, i])
        
        while maxHeap and len(feed) < 10:
            count, tweetId, followingId, i = heapq.heappop(maxHeap)
            feed.append(tweetId)
            if i > 0:
                count, tweetId = self.tweets[followingId][i - 1]
                heapq.heappush(maxHeap, [count, tweetId, followingId, i - 1])
                
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
