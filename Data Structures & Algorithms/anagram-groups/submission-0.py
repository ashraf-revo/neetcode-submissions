from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        def hash_code(s:str)->str:
            freq=Counter(s)
            sorted_s=sorted(freq.items(),key=lambda v:v[0])
            return "-".join([f"{key}-{value}" for key,value in sorted_s])




        groups={}

        for s in strs:
            code=hash_code(s)

            if code not in groups:
                groups[code]=[s]
            else:
                groups[code].append(s)

        return [value for key,value in groups.items()]                






        # 100*100  vs 100+(26*26)