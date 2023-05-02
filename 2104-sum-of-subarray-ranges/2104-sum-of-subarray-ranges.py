class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # another approach o(n^2)
        res = 0
        for i in range(len(nums)):
            min_num = nums[i]
            max_num = nums[i]
            
            for j in range(i+1, len(nums)):
                min_num = min(min_num, nums[j])
                max_num = max(max_num, nums[j])
                
                res +=  max_num - min_num
        return res
# solve using stack next as a follow up
        
        
        """
        #brute force tle o(n^3)
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                count += max(nums[i:j+1])- min(nums[i:j+1])
        return count
            
      
      """
        