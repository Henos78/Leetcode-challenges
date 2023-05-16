class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        temp = list(set(nums))
        ans = 0
        
        for num in temp:
            if num != 0:
                ans += 1
                
        return ans 
    #used the hints to come up with this solution