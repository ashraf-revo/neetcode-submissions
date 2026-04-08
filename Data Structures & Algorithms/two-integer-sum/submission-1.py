class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem={}

        for i in range(len(nums)):
            
            required=target-nums[i]

            if required in mem:

                return [mem[required],i]

            else:

                mem[nums[i]]=i

        return []            
        