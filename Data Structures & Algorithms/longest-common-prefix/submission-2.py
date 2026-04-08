class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""


        for i in range(0,200):
            mem=set()
            for s in strs:
                if len(s)<=i:
                    return prefix
                mem.add(s[i])
            
            if len(mem)!=1:
                return prefix
            prefix+=strs[0] [i]   

        return prefix    