class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        seen={}
        left=0
        current=0

        for i,c in enumerate(s):
            if c in seen and seen[c]>=left:
                left=seen[c]+1
            else:
                current=max(current,i-left+1)
            seen[c]=i    
        return current        