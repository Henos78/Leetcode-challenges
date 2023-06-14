class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        nums =sorted([int(i) for i in s])
        
        new1= str(nums[0])+str(nums[3])
        new2= str(nums[1])+str(nums[2])
        
        return int(new1) + int(new2)
        
        
        
        
        