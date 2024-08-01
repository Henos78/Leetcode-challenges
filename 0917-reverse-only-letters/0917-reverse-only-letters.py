class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
    
        temp = str(s)
        l = [i for i in temp]
        n=len(l)
        l2 =  [0]*n

        temp = re.sub(r'[^a-zA-Z]', '', s)
        temp1= temp[::-1]
        
        for i in range(n):
            if l[i].lower() not in "abcdefghijklmnopqrstuvwxyz":
                l2[i]= l[i]
        
        l3 = [i  for i in temp1]
        
        i,j =0,0 #j -> pointer for l2  , i ->  pointer for l3
        
        while n > j:
            if l2[j] == 0:
                l2[j]=l3[i]
                i+=1
                j+=1
            else:
                j+=1
            
        str1=""
        for i in l2:
            str1 += i
        return str1
                
            
        
        
        
        
        
        
        
        
        
        
        