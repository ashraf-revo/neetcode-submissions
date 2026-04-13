import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def smash(x,y):
            if x==y:
                return 0
            if x<y:
                return y-x
            else:
                return x-y

        h=[]

        for i in stones:
            heapq.heappush(h,i*-1)

        
        while len(h)>1:
            x=heapq.heappop(h)*-1
            y=heapq.heappop(h)*-1
            r=smash(x,y)
            if r !=0:
                heapq.heappush(h,r*-1)
            


        return 0 if len(h)==0 else h[0]*-1    
        
                            