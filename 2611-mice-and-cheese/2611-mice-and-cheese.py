class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        #Solved using different approach
        dif =[[]]*len(reward1)
        res = 0
        
        for i in range(0,len(reward1)):
            dif[i] =[reward2[i]-reward1[i], i]
        
        dif.sort(key =lambda x:x[0])
        print(dif)
        seen = [False]*len(dif)
        for i in range(k):
            res += reward1[dif[i][1]]
            idx = dif[i][1]
            seen[idx]= True
        
        for i in range(len(reward2)):
            if seen[i] == True:
                continue
            res += reward2[i]
            
        return res
           
            
        