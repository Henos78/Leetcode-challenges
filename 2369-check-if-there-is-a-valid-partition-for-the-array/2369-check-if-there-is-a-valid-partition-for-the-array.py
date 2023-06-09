class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False]*(len(nums)+1)
        dp[0]=True
        dp[2]= nums[0] == nums[1]
        
        l=3
        while l<=len(nums):
            if nums[l-1]==nums[l-2]:
                dp[l]|=dp[l-2]

            if nums[l-1]==nums[l-2]==nums[l-3]:
                dp[l]|=dp[l-3]
            if nums[l-1]-nums[l-2]==1 and nums[l-2]-nums[l-3]==1:
                dp[l]|=dp[l-3]
            
            l+=1
            
        return dp[len(nums)]
            