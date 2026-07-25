class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for j in freq.values():
            if j > 1:
                return True
        return False

        