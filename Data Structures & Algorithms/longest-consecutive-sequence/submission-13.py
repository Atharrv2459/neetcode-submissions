class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numset = set(nums)
        # max_cons = 0
        # length = 0
        # for num in numset:
        #     if (num - 1) not in numset:
        #         length = 1
        #         while (num + length) in numset:
        #             length +=1
        #         max_cons = max(max_cons,length)
        # return max_cons
                



        numset = set(nums)
        max_length = 0
        length = 0
        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while(num + length) in numset:
                    length +=1 
                max_length = max(max_length, length)
    
        return max_length



        numset = set(nums)
        max_l = 0
        l = 0
        for num in numset:
            if (num - 1) not in numset:
                l = 1
                while (num + l) in numset:
                    l += 1
                max_l = max(max_l,l)
        return max_l













