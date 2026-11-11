class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lftPrd=[1 for i in range(len(nums))]
        rhtPrd=[1 for i in range(len(nums))]

        for i in range(1,len(nums)):
            lftPrd[i]=lftPrd[i-1]*nums[i-1]
        
        
            
        for i in range(len(nums)-2,-1,-1):
            rhtPrd[i]=rhtPrd[i+1]*nums[i+1]
            
        result=[]
        for i in range(len(nums)):
            result.append(lftPrd[i]*rhtPrd[i])
        return result
