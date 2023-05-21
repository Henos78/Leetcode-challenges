class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        shift = 0 
        
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        
        return left << shift
    
        
        """
        # inital solution got tle
        
        res = left
        
        for i in range(left,right+1):
            res &=i
        return res
        """
       