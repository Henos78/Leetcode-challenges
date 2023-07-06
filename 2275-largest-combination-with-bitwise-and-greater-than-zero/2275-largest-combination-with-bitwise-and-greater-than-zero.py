class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        res =[0]*32
        
        for num in candidates:
            for i in range(0,32):
                if num &(1<<i):
                    res[i]+=1
                    
        return max(res)
        
      
        """
        #first trail, brute force supposed to work but didnt(debug later on)
        res = 0
        count=0
        ans =[]
        for i in range(len(candidates)):
            temp = candidates[i]
            for j in range(i,len(candidates)):
                temp &=candidates[j]
                res = max(res,temp)
                
                if temp == res:
                    count = max(count,j+1)
            ans.append(count)
            count=0
            
               
        print(ans)
        return max(ans)
        """
                
                
            
        