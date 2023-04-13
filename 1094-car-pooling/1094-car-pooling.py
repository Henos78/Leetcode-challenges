class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #Heap solution o(nlogn)
        trips.sort(key= lambda trip: trip[1])
        
        heap = [] # (end, numPass)
        cur = 0
        
        for trip in trips:
            numPass, start, end = trip
            while heap and heap[0][0] <= start:
                cur -= heap[0][1]
                heapq.heappop(heap)
            cur += numPass
            if cur > capacity:
                return False
            heapq.heappush(heap, [end, numPass])
            
        return True
            
            
        
        """
        # Brute force o(n) solution
        change = [0]*1001
        for trip in trips:
            numPass, start, end = trip
            change[start] += numPass
            change[end] -= numPass
            
        cur= 0
        for i in range(1001):
            cur += change[i]
            if cur > capacity:
                return False
            
        return True
            
      """
            
          