import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        nums = []
        for num in stones:
            nums.append(-1*num)
        heapq.heapify(nums)

        while len(nums) > 1:
            x = -(heapq.heappop(nums))
            y = -(heapq.heappop(nums))
            if x != y:
                heapq.heappush(nums,-(x-y))
        if len(nums) == 1:
            return -nums[0]
        else:
            return 0
        