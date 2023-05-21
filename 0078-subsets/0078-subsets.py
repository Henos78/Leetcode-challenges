class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #bit solution
        n = len(nums)
        subsets = []
        for i in range(2 ** n):
            subset = []
            for j in range(n):
                if i >> j & 1:
                    subset.append(nums[j])
            subsets.append(subset)
        return subsets
        