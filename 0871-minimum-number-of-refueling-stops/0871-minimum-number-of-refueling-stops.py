class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # let use max heap and greedy concept to solve it
        res = 0
        maxheap = []
        prev =  0
        
        for position, gas in stations +[[target,0]]:
            startFuel -= (position-prev)
            
            while maxheap and startFuel <0:
                startFuel += -heapq.heappop(maxheap)
                res  +=1
                
            if startFuel <0:
                return  -1
            heapq.heappush(maxheap,-gas)
            prev= position
            
        return res
            
    