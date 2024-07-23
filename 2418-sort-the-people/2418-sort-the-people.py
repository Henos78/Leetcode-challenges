class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        temp = list(zip(names, heights))
        temp1 = sorted(temp, key=lambda x:x[1], reverse=True)
        
        return [name[0]  for name in temp1]
    
        