class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        maxcount = 0
        for r in range(len(s2)):
            l = r
            arr =[]
            for ch in s1:
                arr.append(ch)
            count = 0
            while  l < len(s2) and s2[l] in arr:
                count +=1
                arr.remove(s2[l])
                l += 1
            maxcount = max(maxcount,count)
        if maxcount == len(s1):
            return True
        return False




        