class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        output = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        used = []
        for item,value in freq.items():
            used.append([value,item])
        s_used = sorted(used)
        i = 0
        while i < k:
            output.append(s_used[-1][1])
            s_used.pop()
            i += 1
        return output[::-1]

        
        






            
        
        