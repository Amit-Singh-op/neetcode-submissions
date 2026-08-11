class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s in res:
                res[s].append(strs[i])
            else:
                res[s] = []
                res[s].append(strs[i])
        
        return list(res.values())
        

