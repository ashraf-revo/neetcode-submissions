from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)

        sorted_freq=sorted(list(freq.items()),key=lambda x:x[1],reverse=True)

        return [t[0] for t in sorted_freq[:k]]
