import string
class Solution:
    def validPalindrome(self, s: str) -> bool:



        def is_valid_plandrome(t):
            left=0
            right=len(t)-1
            while left<right:
                if t[left]!=t[right]:
                    return False
                left +=1
                right -=1    
            return True 

        left=0
        right=len(s)-1
        
        while left<right:
            if s[left]!=s[right]:
                s1=s[left:right]
                s2=s[left+1:right+1]
                return is_valid_plandrome(s1) or is_valid_plandrome(s2)
            left +=1
            right -=1    
        return True 
