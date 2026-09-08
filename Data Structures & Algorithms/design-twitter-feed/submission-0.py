class Twitter:

    def __init__(self):
        self.following = defaultdict(set) #stores followings of user_id
        self.tweets = defaultdict(list)  #stores tweets of user_id (time, tweetId)
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        #stores newest tweets at end
        self.tweets[userId].append((self.time,tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []

        #Put all tweets into heap
        for user in users:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap,(-time, tweetId))
        result = []

        while heap and len(result) < 10:
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
