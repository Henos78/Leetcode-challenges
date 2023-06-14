class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res =0
        s= str(n)
        
        nums = [int(i) for i in s]
        
        for i in range(len(nums)):
            if i%2==0:
                res  += nums[i]
            else:
                res -=nums[i]
        
        return res