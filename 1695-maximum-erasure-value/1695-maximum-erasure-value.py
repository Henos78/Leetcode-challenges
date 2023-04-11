class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # approach two using sliding window
        arr= set()
        l, r = 0,0
        res = 0
        curSum =0
        
        for r in range(len(nums)):
            
            while nums[r] in arr:
                arr.remove(nums[l])
                curSum -= nums[l]
                l+=1
                
            arr.add(nums[r])
            curSum += nums[r]
            
            res = max(res, curSum)
            
        return res
            
        
        
        
        
        """
      #Brute force approach
        arr = set()
        res = 0
        
        for i in range(len(nums)):
            if nums[i] in arr and nums[i] != nums[i-1]:
                temp = list(arr)
                res= max(res, sum(temp))
                
                arr = set()
                arr.add(nums[i-1])
                arr.add(nums[i])
                
    
            arr.add(nums[i])
        
        temp = list(arr)
        res= max(res, sum(temp))
            
        return res  
        """
        
        