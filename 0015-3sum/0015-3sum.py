class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        # fix the first element of the triplet and use a two-pointer approach to find the remaining two elements whose sum is equal to the negative of the fixed element
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    #we do this to avoid duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                elif temp < 0:
                    l += 1
                else:
                    r -= 1
        return res
