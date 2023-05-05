class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #simply using a dictionary we will map the value and the index
        # dic = dict(map(lambda x:(x[1],x[0]+1), enumerate(t)))
        
        dic = {}
        
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] +=1
                
        for ch in t:
            if ch not in dic or dic[ch]==0:
                return ch
            else:
                dic[ch] -=1
