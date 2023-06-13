class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        res =  0
        nums.sort()
        n=len(nums)
        mid = nums[n//2]
        
        for num in nums:
            res+= abs(num-mid)
            
        return res