class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        temp =sorted(set(arr))
        res =[]
        dic={}
        
        for i in range(len(temp)):
            dic[temp[i]]=i+1
            
        for num in arr:
            res.append(dic[num])
    
        return res