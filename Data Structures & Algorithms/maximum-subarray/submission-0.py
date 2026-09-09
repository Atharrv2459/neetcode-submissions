class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(current_sum + nums[i],nums[i])
            res = max(current_sum,res)
        return res