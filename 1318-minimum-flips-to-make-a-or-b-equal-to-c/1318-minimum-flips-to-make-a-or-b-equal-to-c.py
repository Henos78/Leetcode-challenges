class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        flip = 0
        
        while a or b or c:# the last bit of c is either 0 or 1 after performing a|b
            #here we find the bit of all the numbers 
            lastA = a&1
            lastB = b&1
            lastC = c&1
            
            if lastC ==0:
                flip += (lastA+lastB) #we simply add the last bit representaions  of  a and b
            else:
                flip += not(lastA | lastB) #here it  means lastC = 1 this to happen lastA and lastB are 0 so at least one should be 1 so we do not(lastA|lastB)
             
            #then we finally do right shift to all the numbers
            a >>=1
            b >>=1
            c >>=1
            
        return flip
        