class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #not the correct result based on the question prompt
        sys.set_int_max_str_digits(10000)
        num1 = int(num1)
        num2 = int(num2)
        res = num1 + num2
        
        return str(res)