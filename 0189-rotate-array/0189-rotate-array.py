class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        # using a concept called cyclic dependency/replacements 
        nums.reverse()
        
        k = k%len(nums)# this will solve the edge case 
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
        
        #  brute force without using additional space 
        # i = 1
        # j = len(nums)-k
        # while i <=j:
        #     k = 0
        #     nums.append(nums[k])
        #     nums.remove(nums[k])
        #     i+=1
            
            
        
            
                
                