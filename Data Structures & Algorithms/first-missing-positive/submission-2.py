class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        ##. 6,4,2,6,7,8,5,2,7,9,10,11,12,15,14,1,2,5
        ## assume every item is not exi
        ## smallest defination mean 1,2,3
        ## suppose 1 is missing


        clone=set(nums) ## mem for Positive numbers Only

        ## nums should be from 1,to len(nums)


        for i in range(1,len(clone)+1): ## will visit from 1 to end where 1 is first Positove number

            if i not in clone:
                return i

        return len(clone)+1        


