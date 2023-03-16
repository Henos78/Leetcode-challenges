class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]
            
        print(left_prod)
        print(right_prod)

        for i in range(len(nums)):
            res[i] = left_prod[i] * right_prod[i]

        return res