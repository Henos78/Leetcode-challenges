class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
    #Do this question again by fully understaning it!
        return self.helper([i for i in range(1, n+1)])
    def helper(self,nums):
        if len(nums)<=2:
            return nums
        return self.helper(nums[::2])+ self.helper(nums[1::2])
        
