from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max_seen=len(nums)//3
        freq=Counter(nums)
        return [key for key,value in freq.items() if value>max_seen]