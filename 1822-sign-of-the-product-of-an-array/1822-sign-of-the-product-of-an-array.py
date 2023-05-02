class Solution:
    def arraySign(self, nums: List[int]) -> int:
        #brute force t.c: o(n) s.c: o(1)
        if 0 in nums:
            return 0
        
        for i in range(len(nums)):
            if nums[i] <0:
                nums[i] = -1
            else:
                nums[i] = 1
                
        count = Counter(nums)
        
        if count[-1] % 2 != 0:
            return -1
        else:
            return 1
        
        