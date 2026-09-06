import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heap.append(-(num))
        heapq.heapify(heap)

        for i in range(k):
            x = heapq.heappop(heap)
            if i == k - 1:
                return -(x)