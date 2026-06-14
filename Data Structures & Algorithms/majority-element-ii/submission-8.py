from collections import Counter
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max_seen=len(nums)//3
        freq=defaultdict(int)
        result=set()

        for n in nums:
            freq[n] +=1
            if freq[n]>max_seen:
                result.add(n)
        return list(result)    