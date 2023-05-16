class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using bit approach 
        
        missed = len(nums)
        total = 0
        
        for i in range(len(nums)):
            missed ^= nums[i]
            total ^=i
            
        return total ^ missed
            
        
        
       