class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = [str(i) for i in nums]
        temp =""
        for i in res:
            temp +=i
            
        return abs(sum([int(i) for i in temp])-sum(nums))
        