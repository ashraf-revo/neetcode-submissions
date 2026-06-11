class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique_nums=set(nums)


        def count_sequance(i:int):
            c=0
            while i in unique_nums:
                c +=1
                i +=1
            return c      

        m=0

        for i in nums:
            c=count_sequance(i)
            if c>m:
                m=c


        return m        