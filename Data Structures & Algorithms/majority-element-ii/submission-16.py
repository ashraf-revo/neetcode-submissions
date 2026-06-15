class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        target=len(nums)/3
        c1=c2=None
        cc1=cc2=0
        for i in nums:
            if cc1==0:
                cc1 =1
                c1=i
            elif c1==i:
                cc1 +=1
            elif cc2==0:
                cc2 =1
                c2=i
            elif c2==i:
                cc2 +=1
            else:
                cc1 -=1
                cc2 -=1



        print(c1,c2)

        return [i for i in set([c1,c2]) if i !=None and nums.count(i)>target]


        