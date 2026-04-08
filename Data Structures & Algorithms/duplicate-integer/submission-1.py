from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        r=len(set(nums))

        return n!=r        
