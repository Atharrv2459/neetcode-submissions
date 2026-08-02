class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n= len(heights)
        
        for i in range(n):
            height = heights[i]
            right_most = i + 1
            while right_most < n and heights[right_most] >= height:
                right_most = right_most + 1
            left_most = i -1
            while left_most >= 0 and heights[left_most] >= height:
                left_most = left_most - 1
                
              
            right_most = right_most - 1
            left_most =left_most + 1
            maxArea = max(maxArea, height * (right_most-left_most+1))
        return maxArea
        
        

        