import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        distance = []
        dist_dict = {}
        output = []
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            distance.append(dist)
            heapq.heappush(heap,(dist,point))
        for i in range(k):
            x = heapq.heappop(heap)
            output.append(x[1])

        
        
        return output
        