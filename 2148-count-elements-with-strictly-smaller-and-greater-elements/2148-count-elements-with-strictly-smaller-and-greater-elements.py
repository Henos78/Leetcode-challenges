class Solution:
    def countElements(self, nums: List[int]) -> int:
        res = 0
        maxNum = max(nums)
        minNum = min(nums)
        
        for num in nums:
            if num>minNum  and num <maxNum:
                res += 1
        return res
        
     