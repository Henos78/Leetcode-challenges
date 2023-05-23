class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bnum = bin(n)[2:]
        
        if  n >2**31-1:
            return False
        
        l,r =0,1
        
        while r < len(bnum):
            if bnum[l]==bnum[r]:
                return False
            l +=1
            r +=1
        return True