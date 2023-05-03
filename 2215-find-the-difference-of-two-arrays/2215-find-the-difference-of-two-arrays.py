class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = []
        res2 = []
        nums11 = list(set(nums1))
        nums22 = list(set(nums2))
        
        for num in nums11:
            if num not in nums22:
                res1.append(num)
                
        for num in nums22:
            if num not in nums11:
                res2.append(num)
                
        return [res1, res2]