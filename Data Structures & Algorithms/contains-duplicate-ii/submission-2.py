class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        k=min(k,len(nums))

        for i in range(len(nums)-k+1):
            sub=nums[i:i+k+1]
            if len(sub) !=len(set(sub)):
                return True

        return False    