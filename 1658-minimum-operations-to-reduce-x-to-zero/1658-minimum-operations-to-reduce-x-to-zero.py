class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i,res,temp =0,float("-inf"),0
        target = sum(nums) - x
        
        for j in range(len(nums)):
            temp += nums[j]
            
            while i<=j and temp > target:
                temp -=nums[i]
                i+=1

            if temp ==target:
                res = max(res,j-i+1)
        
        if res == float("-inf"):
            return -1
        else:
            return len(nums)-res
                