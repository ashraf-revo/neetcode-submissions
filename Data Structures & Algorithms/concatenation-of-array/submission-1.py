class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[None]*n*2


        result[0:n]=nums
        result[n:n*2]=nums

        return result