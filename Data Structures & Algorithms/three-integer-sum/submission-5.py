class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        s_num = sorted(nums)
        for i in range(len(s_num)):
            k = len(s_num) - 1
            j = i + 1
            while j < k:
                total = s_num[i] + s_num[j] + s_num[k]
                if total == 0:
                    res.add((s_num[i],s_num[j],s_num[k]))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
        return [list(t) for t in res]

