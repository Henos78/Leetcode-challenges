class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        """
        #trial one error 
        n  = len(matrix)
        for mat in matrix:
            temp = sorted(matrix[0])
            temp2= sorted(mat)
            
            temp3 =[ i for i in range(1,n+1)]
            
            for j in range(0,n):
                if temp[j] !=temp3[j] or temp2[j] != temp3[j] or temp[j] !=temp2[j]:
                    return False
                
            #for i in range(0,n):
              #  if temp[i] != temp2[i]:
                #    return False
                    
        return True
        
        
        """
        #
        n = len(matrix)
        for i in range(n):
            temp = sorted(set(matrix[i]))
            if len(temp) != n:
                return False
            
            temp2 = set()
            for j in range(n):
                temp2.add(matrix[j][i])
            if len(temp2) !=n:
                return False
                
           
        return True
                
                
            
        