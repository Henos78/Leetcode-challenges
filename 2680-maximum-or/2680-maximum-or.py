class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
    
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] | nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] | nums[i+1]

        return max(pre | (num << k) | suf for pre, num, suf in zip(prefix, nums, suffix))
    
    
    
        """
                #second trial
        pre = [0]*len(nums)
        suf = [0]*len(nums)

        pre[0]=nums[0]
        suf[-1]=nums[-1]
        
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] | nums[i]
        
        for i in range(len(nums)-2,-1,-1): 
            suf[i]= suf[i+1] | nums[i]
          
        result = 0
        for i in range(len(nums)):
            max_value = (nums[i] | (nums[i] << k))
            if i > 0:
                max_value |= pre[i-1]
            if i < len(nums)-1:
                max_value |= suf[i+1]
            result = max(result, max_value)

        return result
        """
        
       
        
       
        """
        #first trial:  only worked for 1 testcase with k =1
        pre = [0]*len(nums)
        suf = [0]*len(nums)
        temp =0
        # pre[0]=nums[0]
        # suf[-1]=nums[-1]
        
        for i in range(1,len(nums)):
            pre[i] = temp | nums[i-1]
    
        temp=0
        for i in range(len(nums)-2,-1,-1): 
            suf[i]= temp | nums[i+1]
            
            
        print(pre)
        print(suf)
        maxOr = 0
        for i in range(len(nums)):
            num = nums[i] << k
            prefix = pre[i]
            suffix = suf[i]

            maxOr = max(maxOr, num | prefix | suffix)

        return (maxOr)
        """
 
       
            
        