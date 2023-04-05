class Solution:
    def reverse(self, x: int) -> int:
        if  x< 0:
            res = "-"
            temp = str(abs(x))[::-1]
            res += temp
            res = int(res)
            if res < -2**31:
                return 0
            return res
        else:
            res = int(str(x)[::-1])
            if res > 2**31:
                return 0
            return res
       