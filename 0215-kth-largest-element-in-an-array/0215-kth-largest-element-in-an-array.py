class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        while len(minHeap) >k:
            heapq.heappop(minHeap)
            
        if len(minHeap) == k:
            return minHeap[0]
        
        
        