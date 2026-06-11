class Twitter:

    def __init__(self):
        self.count = 0
        self.following = defaultdict(set) # set of all people following
        self.tweetMap = defaultdict(list) # userId -> [count, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []

        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.tweetMap:
            # last index to get most recent tweet of that user
                index = len(self.tweetMap[user]) - 1
                # get the time and tweetId for that user at the last index
                count, tweetId = self.tweetMap[user][index]
                # push their information into the heap
                heapq.heappush(maxHeap, [count, tweetId, user, index])
        
        while len(res) != 10 and maxHeap:
            # get the most recent tweet and add to res
            count, tweetId, user, index = heapq.heappop(maxHeap)
            print(tweetId, '\n')
            res.append(tweetId)

            # if idx >= 0, the user has more tweets,
            # add those to the heap as they might be more recent
            if index > 0:
                count, tweetId = self.tweetMap[user][index - 1]
                heapq.heappush(maxHeap, [count, tweetId, user, index - 1])
        
        return res


            


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        
