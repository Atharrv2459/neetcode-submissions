class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        output = []
        for word in strs:
            s = "".join(sorted(word))
            if s not in res:
                res[s] = [word]
            else:
                res[s].append(word)
        for value in res.values():
            output.append(value)
        return output

                
                


        