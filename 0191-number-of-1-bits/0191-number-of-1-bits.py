class Solution:
    def hammingWeight(self, n: int) -> int:
        # using bit manipulation
        
        count=0
        while n:
            #perform bitwise AND and add the result to count
            count+= n &1
            n >>=1  #right shift with 1
        return count
        
      
        
        