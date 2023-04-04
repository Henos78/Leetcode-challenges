class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num1 = set(nums)
        num2 = list(map(int, num1))
        num2.sort()
        if len(num2) < 3:
            return max(num2)
        return num2[len(num2)-3]
        
        
        