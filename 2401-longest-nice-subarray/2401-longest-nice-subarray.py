class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l,res,curAND=0,0,0
        
        for r in range(len(nums)):
            while curAND & nums[r] != 0:
                curAND ^= nums[l]
                l+=1 
                
            curAND ^= nums[r]
            res = max(res,(r-l+1))
            
        return res
        