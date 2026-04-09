class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lower=0
        upper=len(nums)-1

        while lower<=upper:
            middle=lower+(upper-lower)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                lower=middle+1
            else:
                upper=middle-1        

        return -1