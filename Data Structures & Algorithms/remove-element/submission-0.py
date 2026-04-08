class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ## will define two pointers [left,right]=0
        ## increment right if equal val
        ## if not swap and increment right and left

        left=0
        for i in range(len(nums)):
            if val!=nums[i]:
                nums[left]=nums[i]
                left +=1

        return left        