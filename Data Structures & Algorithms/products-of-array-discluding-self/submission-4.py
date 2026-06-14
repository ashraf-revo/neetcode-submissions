class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        left_map={}
        right_map={}

        count_zeros=0
        for i in range(len(nums)):

            if nums[i]==0:
                count_zeros +=1
            if count_zeros>=2:
                return [0]*len(nums)    

            inverted_i=len(nums)-i-1
            if i==0:
                left_map[i]=1
                right_map[inverted_i]=1
            else:
                left_map[i]=nums[i-1]*left_map[i-1]
                right_map[inverted_i]=nums[inverted_i+1]*right_map[inverted_i+1]



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

            result.append(left_map[i] * right_map[i])
        return result