class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])
            temp = str(nums[i])[::-1]
            seen.add(int(temp))
            
        return len(seen)
        
    
        
        