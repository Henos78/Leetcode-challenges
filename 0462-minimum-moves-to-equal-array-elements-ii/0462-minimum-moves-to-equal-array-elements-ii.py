class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        res =  0
        nums.sort()
        n=len(nums)
        mid = nums[n//2] #simply find the median value
        
        for num in nums:
            res+= abs(num-mid)# add  tbe absolute diff between the num and the median
            
        return res