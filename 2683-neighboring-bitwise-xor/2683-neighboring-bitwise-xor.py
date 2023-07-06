class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        n =len(derived)
        res= 0
        
        if n ==1 and derived[0]==0:
            return True
        
        for num in derived:
            res ^= num
            
        return res==0 
    
        """
        #first appraoch
        original =[]
        
        for i in range(n):
            temp = i+1
            if temp <=n-1:
                original.append(derived[i]^derived[temp])
            if i == n-1:
                original.append(derived[i]^derived[0])
                
        print(original)
        return True
        
        """
        
        