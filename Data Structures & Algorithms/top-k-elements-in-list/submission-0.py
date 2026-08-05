class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        used =[]
        result = []
        freq={}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        for number,value in freq.items():
            used.append([value,number])
        used.sort()

        while len(result)<k:
            result.append(used.pop()[1])
        return result        

        
        






            
        
        