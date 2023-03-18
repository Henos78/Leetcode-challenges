class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        prefix_sum = [0]
        
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        stack = [-1]
        max_min_product = 0
        for i in range(n):
            while stack[-1] != -1 and nums[stack[-1]] >= nums[i]:
                j = stack.pop()
                max_min_product = max(max_min_product, nums[j] * (prefix_sum[i] - prefix_sum[stack[-1] + 1]))
            stack.append(i)

        while stack[-1] != -1:
            j = stack.pop()
            max_min_product = max(max_min_product, nums[j] * (prefix_sum[n] - prefix_sum[stack[-1] + 1]))

        return max_min_product % MOD