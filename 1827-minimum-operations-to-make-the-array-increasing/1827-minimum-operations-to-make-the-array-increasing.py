class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count =0
        
        l,r =0,1
        
        while r <len(nums):
            if nums[r]<=nums[l]:
                temp = nums[l]-nums[r]+1
                nums[r] += temp
                count += temp
            else:
                l+=1
                r+=1
                
        return count