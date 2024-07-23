class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    
        temp =[]
        for i in range(len(names)):
            temp.append([names[i], heights[i]])
        print(temp)
        
        temp1  = sorted(temp, key=lambda x:x[1], reverse=True)
        print(temp1)
        
        res = []
        
        for j in  range(len(temp1)):
            res.append(temp1[j][0])
            
        return res
        
        
        