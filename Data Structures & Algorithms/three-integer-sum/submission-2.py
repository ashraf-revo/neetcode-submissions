class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        m={}

        for i in range(len(nums)):
            m[nums[i]]=i
        
        result=[]
        hashs=set()

        def hash(arr):
            return f"{arr[0]}-{arr[1]}-{arr[2]}"

        for i in range(len(nums)):
            for l in range(i+1,len(nums)):
                
                target=(nums[i]+nums[l])*-1
                
                if target in m and m[target] not in [i,l]:

                    t=sorted([nums[i],nums[l],target])
                    h=hash(t)
                    if h not in hashs:
                        result.append(t)
                        hashs.add(h)

        return result