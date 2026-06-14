class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)
        n=len(nums)

        left_cur = 1
        right_cur = 1


        for i in range(0, len(nums)):
            result[i] *= left_cur
            left_cur *= nums[i]

            i_i=n-i-1
            result[i_i] *= right_cur
            right_cur *= nums[i_i]

        return result
