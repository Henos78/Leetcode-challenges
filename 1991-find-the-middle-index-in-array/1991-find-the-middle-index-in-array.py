class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = [0]*len(nums)
        pre_sum[0] = nums[0]
        
        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i-1] + nums[i]

        
        for i in range(len(nums)):
            left = pre_sum[i]-nums[i]
            right = pre_sum[len(nums)-1]- pre_sum[i]
            
            if left == right:
                return i
            
        return -1
        
        