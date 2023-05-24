class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic ={}
        for  ch in s:
            if ch not in dic:
                dic[ch] =1
            else:
                dic[ch] +=1
        temp =[]      
        for val in dic:
            temp.append(dic[val])
    
        return True if len(set(temp))==1 else False
            
            
            
        