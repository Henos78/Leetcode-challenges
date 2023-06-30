class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        res = 2

        for i in range(n):
            for j in range(i):
                temp = nums[i] - nums[j]
                if temp in dp[j]:
                    dp[i][temp] = dp[j][temp] + 1
                else:
                    dp[i][temp] = 2
                res = max(res, dp[i][temp])

        return res
