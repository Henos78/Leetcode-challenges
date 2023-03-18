class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        s = set(nums)
        res = ''

        def backtrack(i, cur):
            nonlocal res
            if i == n:
                if cur not in s:
                    res = cur
                return
            backtrack(i+1, cur+'0')
            backtrack(i+1, cur+'1')

        backtrack(0, '')
        return res