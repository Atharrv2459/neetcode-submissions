class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        used = []
        for i,num in enumerate(numbers):
            used.append([num,i])
        s_used = sorted(used)
        l = 0
        r = len(s_used) - 1
        while l < r:
            if s_used[l][0] + s_used[r][0] == target:
                return [s_used[l][1] + 1,s_used[r][1] + 1]
            elif s_used[l][0] + s_used[r][0] < target:
                l += 1
            else:
                r -= 1
        
        