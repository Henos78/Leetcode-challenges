class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,res,temp=0,float("inf"),0
        
        for j in range(len(nums)):
            temp += nums[j]
               
            while temp >= target:
                res = min(res,(j-i+1))
                temp -=nums[i]
                i+=1
                           
        if res == float("inf"):
            return 0
        else:
            return res
                         
       
                    
                          
                           
        
        
        