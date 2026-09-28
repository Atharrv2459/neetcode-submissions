class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l,r):
            count = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        max_count = 0
        for i in range(len(s)):
            max_count += expand(i,i)
            max_count += expand(i,i+1)
        return max_count

        
        