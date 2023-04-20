class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x2 = str(x[::-1])
        
        return x == x2
        