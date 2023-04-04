class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        #Heap solution
        arr = list(map(int, nums))
        heap = arr
        heapq.heapify(heap)
        
        while len(heap) > k:
            heapq.heappop(heap)
            
        return str(heap[0])