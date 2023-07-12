class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res =[]
        
        k = 2**maximumBit-1  
        temp = 0
        
        for i in range(len(nums)):
            temp^=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res.append(temp^k)
            temp^=nums[i]
            
        return res
        
        
        
        
        """
        res = []
        n = len(nums)
        
        while n>0:

            k =0
            max_k = float("-inf")
            while k < 2**maximumBit:
                temp =k
                for i in range(len(nums)):
                    temp^=nums[i]
                    
                max_k =max(max_k,k)
                k+=1
                
            res.append(max_k)
            max_k = float("-inf")
            if len(nums)>0:
                nums.pop()
            else:
                break
        
        return res
                
                
        """