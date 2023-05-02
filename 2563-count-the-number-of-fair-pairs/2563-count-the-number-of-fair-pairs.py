class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # using two pointers
        nums.sort()
        count = 0
        
        #check for the upper
        l, r = 0, len(nums)-1
        while l <r:
            temp = nums[l] + nums[r]
            if temp > upper:
                r -= 1
            else:
                count += r -l
                l += 1
                
                
         # Check for the lower      
        l, r = 0, len(nums)-1
        while l <r:
            temp = nums[l] + nums[r]
            if temp > lower-1:
                r -= 1
            else:
                count -= r -l
                l += 1
                
        return count
       