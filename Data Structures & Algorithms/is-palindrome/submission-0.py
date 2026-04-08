import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid=string.ascii_letters + string.digits
        left=0
        right=len(s)-1

        while left<right:
            if s[left] not in valid:
                left +=1
                continue
            if s[right] not in valid:
                right -=1
                continue
            left_val=s[left].lower()
            right_val=s[right].lower()    
            if left_val !=right_val:
                return False
            left +=1
            right -=1        


        return True