class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rcount = 0
        lcount = 0
        res = 0
        
        for i in range(len(s)):
            if s[i] =='L':
                lcount +=1
            elif s[i]=='R':
                rcount +=1
                
            if lcount ==  rcount:
                res +=1
                lcount =0
                rcount =0
                
        return res