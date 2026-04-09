class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mp=0
        # define two pointers left,right
        # left should equal lowest previous value , 
        # right is prices iterations
        # for every iteration get profit of right - left
        # if profit is more that mp , clone mp
        # left=min(left,right)

        mp=0
        left,right=0,1
        while right<len(prices):
            rval=prices[right]
            lval=prices[left]
            nmp=rval-lval
            mp=max(mp,nmp)

            if rval<lval:
                left=right

            right +=1
        return mp