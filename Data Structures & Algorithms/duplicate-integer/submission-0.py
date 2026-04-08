from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem=defaultdict(int)

        for i in nums:
            mem[i] +=1
            if mem[i]>1:
                return True
        return False        
