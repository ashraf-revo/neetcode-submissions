class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        window=0
        i=0
        while i<len(nums):
            s=0

            for j in range(i,len(nums)):

                s+=nums[j]

                if s>=target:
                    window =min(window,j-i+1)
                    if window==0:
                        window=j-i+1
                    break
            i+=1

        return window

        