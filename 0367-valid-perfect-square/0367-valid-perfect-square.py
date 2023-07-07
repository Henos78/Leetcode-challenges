class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        tmp =num**0.5
        
        if tmp == int(num**0.5):
            return True
        else:
            return False