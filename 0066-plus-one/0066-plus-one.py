class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        temp = ""
        for i in range(len(digits)):
            temp += str(digits[i])
         
        num = int(temp)
        res = num + 1
        res = str(res)
        
        return [int(i) for i in res]
        
            
        