class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        prefix =[0]*n
        suffix =[0]*n
        
        setPre = set()
        setSuf = set()
        
        res = 0
        
        for i in range(n):
            setPre.add(s[i])
            setSuf.add(s[n-1-i])
            
            prefix[i] = len(setPre)
            suffix[n-1-i] = len(setSuf)
            
        for i in range(1,n):
            if prefix[i-1]==suffix[i]:
                res+=1
                
        return res
            
            
                        