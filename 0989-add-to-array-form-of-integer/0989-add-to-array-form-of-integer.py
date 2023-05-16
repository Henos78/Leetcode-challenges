class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(1000000)
        temp = ""
        
        for i in range(len(num)):
            temp += str(num[i])
            
        res = int(temp)+k
        
        return [int(i) for i in str(res)]
        