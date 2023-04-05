class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        res = []
        nums.sort()
        
        r = 0
        l = len(nums)-1
        
        while r < l:
            res.append(nums[r]+nums[l])
            r +=1
            l -= 1
        
        return max(res)
            
    
    

    
        
        