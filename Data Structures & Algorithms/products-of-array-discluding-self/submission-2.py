class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        left_map={}

        for i in range(len(nums)):
            if i==0:
                left_map[i]=1
            else:
                left_map[i]=nums[i-1]*left_map[i-1]


        print(left_map)

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

            result.append(left_map[i] * calc_right(i))
        return result