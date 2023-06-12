class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = gcd(len(str1),len(str2))
        return str1[:n] if str1+str2 == str2+str1 else ""
    
    
        """
        #First trial it was supposed to work  but  didnt for s1=ABCDEF  AND  S2= ABJDEF
        res = set()
        a,b = len(str1), len(str2)
        i=0
        
        if a<b:
            while i<a:
                if str1[i]==str2[i] and str1[i] not in res:
                    res.add(str1[i])
                else:
                    break
                i+=1
        else:
            while i<b:
                if str2[i]==str1[i] and str2[i] not in res:
                    res.add(str2[i])
                else:
                    break
                i+=1
                
        return "".join(sorted(res))
        """