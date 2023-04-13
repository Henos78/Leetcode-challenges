class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        arr = set(nums)
        count = 0
        
        for num in nums:
            #num+diff in arr and num + diff*2 : is simply just the property of artimetic triplets
            if num+diff in arr and num + diff*2 in arr: 
                count += 1
                
        return count
    
    
        
        
                        
        
        
       
#         # two pointer approach
        
#         i,j,k =0,1,2
#         count = 0
        
#         while k < len(nums):
            
#             if nums[j]-nums[i] == diff and nums[k]-nums[j] == diff:
#                 count +=1
#                 i +=1
#                 j +=1
#             elif nums[j]-nums[i] < diff or nums[k]-nums[j]< diff:
#                 k+=1
            

#             else: 
#                 i+=1
#                 j+=1
#                 k+=1

#         return count
    
    
        """
        #brute force (trial 1)
        count= 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if abs(nums[k]-nums[j]) == diff and abs(nums[j]-nums[i]) == diff:
                        count +=1
                        
                        
        return count
        
        """
        
        