class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        #we use max heap t.c: nlogn
        
        heap = [(-nums[0],0)]
        
        for i in range(1, len(nums)):
            while heap[0][1] < i-k:
                heappop(heap)
                
            max_val = heap[0][0]
            heappush(heap, (max_val-nums[i],i))
            
            if i == len(nums)-1:
                return -(max_val-nums[i])
            
            
        return nums[0]
                
        