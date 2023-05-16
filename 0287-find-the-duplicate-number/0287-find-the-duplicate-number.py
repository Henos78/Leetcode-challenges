class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using two pointers
        nums.sort()
        l,r=0,1
        
        while r <len(nums):
            if nums[l]==nums[r]:
                return nums[l]
                break
            l +=1
            r +=1
        