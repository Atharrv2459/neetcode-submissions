class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1][1]]:
                x = stack.pop()
                res[x[1]] = i - x[1]
            stack.append([temperatures[i],i])
        return res

        

        