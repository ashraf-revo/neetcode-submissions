class Solution:
    def mySqrt(self, n: int) -> int:
        lower=0
        upper=n

        while lower<=upper:
            middle=lower+(upper-lower)//2

            p=middle * middle
            print(lower,upper,middle,p)

            if p==n:
                return middle
            elif p>n:
                upper=middle-1
            else:
                lower=middle+1
        return lower-1
