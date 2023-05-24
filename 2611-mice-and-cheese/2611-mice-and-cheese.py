class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        res = 0
        heap = []
        seen = [False]*len(reward1)
        for i in range(0,len(reward1)):
            heap.append([(reward2[i]-reward1[i]),i])
        heapq.heapify(heap)
        

        while k:
            i = heapq.heappop(heap)[1]
            res += reward1[i]
            k -=1
            seen[i] = True
            
        for i in range(0,len(reward2)):
            if seen[i] == True:
                continue
            res += reward2[i]
            
        return res
        
        
        
        """
        #first approach
        reward1.sort()
        reward2.sort(reverse =True)
        
        res = 0
        l, r=0, len(reward2)-1
        
        while k:
            res +=reward1[r]
            res += reward2[l]
            l +=1
            r -=1
            k -=1
        
        return res
        
        """
        