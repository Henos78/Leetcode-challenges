class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = []
        for i in nums:
            nums2.append(i)
            
        for i in nums2:
            nums.append(i)
        return nums