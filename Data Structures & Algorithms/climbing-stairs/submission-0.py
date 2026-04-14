
class Solution:
    def climbStairs(self, n: int) -> int:
        # n =2 [1+1,2]          =2
        # n =3 [1+1+1,2+1+1+2]          =3
        # n =4 [1+1+1+1,2+2,2+1+1,1+2+1,1+1+2] =5
        mem={1:1,2:2}
        if n in mem:
            return mem[n]

        for i in range(3,n+1):
            mem[i]=mem[i-1]+mem[i-2]

        return mem[n]
