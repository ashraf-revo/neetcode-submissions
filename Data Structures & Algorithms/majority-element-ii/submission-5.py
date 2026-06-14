from collections import Counter
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max_seen=len(nums)//3
        freq=defaultdict(list)
        result=[]

        for n in nums:
            if n in freq:
                freq[n] +=1
            else:
                freq[n]=1  
            if freq[n]>max_seen and n not in result:
                result.append(n)
        return result    