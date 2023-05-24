class Solution:
    def maximum69Number (self, num: int) -> int:
        val = [i for i in str(num)]
        
        for i in range(len(val)):
            if val[i] =='6':
                val[i] = '9'
                break
                
        res = ""
        for i in val:
            res += i
        return int(res)