class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        
        i =0
        while n:
            if i%2==0 and n&1:
                even +=1
            if i%2 != 0 and n&1:
                odd +=1
            i +=1
            n >>=1
        return [even, odd]
            