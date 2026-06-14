class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        


        def calc_left(i):
            result=1

            for i in range(0,i):
                result *=nums[i]
            return result    

        def calc_right(i):
            result=1

            for i in range(i+1,len(nums)):
                result *=nums[i]
            return result    


        result=[]
        for i in range(len(nums)):

            left=calc_left(i)
            right=calc_right(i)

            result.append(left * right)
        return result