class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = [str(i) for i in nums]
        temp =""
        for i in res:
            temp +=i
            
        return [int(i) for i in temp]
        
        