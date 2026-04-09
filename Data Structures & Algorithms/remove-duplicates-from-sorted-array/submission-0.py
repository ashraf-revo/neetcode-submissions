class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    #   Input: nums = [1,1,2,3,4]
    #   Output: [1,2,3,4]

    # steps
    # define two pointers left , and right with indexs= 0 , 1
    # compare values in left and right 
    # if equal inc right only
    # if not clone incremnt left and clone the incrment right


        left=0
        right=1

        while right<len(nums):

            if nums[left]==nums[right]:
                pass
            else:
                left +=1
                nums[left]=nums[right]    
            right +=1
        print(nums,left)    
        return left+1    