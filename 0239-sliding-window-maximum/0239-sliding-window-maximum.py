class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #solution 2 using heap
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        
        res = [-heap[0][0]]
        
        
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap and heap[0][1] <= i-k:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])
        
        return res
        
        
        
        
        
        
        """
        #brute force using two pointers (roughly the concept is this but not correct)
        
        res= []
        r = k
        for l in range(len(nums)):
            while r <= len(nums):
                temp = nums[l:r]
                res.append(max(temp))
                r +=1
            
        return res
        """
        
        