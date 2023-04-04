class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #Heap solution 
        num1 = set(nums)
        num2 = list(map(int, num1))
        
        if len(num2) < 3:
            return max(num2)
        heap = num2
        heapq.heapify(num2)
        while len(heap) > 3:
            heapq.heappop(heap)
            
        return heap[0]
        
        
        