import string
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_valid_plandrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l +=1
                r -=1    
            return True 

        left=0
        right=len(s)-1
        
        while left<right:
            if s[left]!=s[right]:
                s1=s[left:right]
                s2=s[left+1:right+1]
                return is_valid_plandrome(left,right-1) or is_valid_plandrome(left+1,right)
            left +=1
            right -=1 
        return True 
