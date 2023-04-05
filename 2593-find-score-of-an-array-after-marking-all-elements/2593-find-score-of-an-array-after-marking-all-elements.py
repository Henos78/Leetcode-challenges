class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        mark = set()

        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        
        while heap:
            num, i = heapq.heappop(heap)
            if i not in mark:
                score += num
                if i-1>=0:
                    mark.add(i-1)
                if i+1<len(nums):
                    mark.add(i+1)
                mark.add(i)
                
        return score
        

       
#         #brute force
#         score = 0
#         mark = set()
        
#         while len(mark)<len(nums):
#             temp = float("inf")
#             idx = -1
            
#             for i in range(len(nums)):
#                 if i not in mark and nums[i] < temp:
#                     temp = nums[i]
#                     idx = i
#             score += temp
#             mark.add(idx)
            
#             if idx-1 >= 0 and idx-1 not in mark:
#                 mark.add(idx-1)
#             if idx + 1 < len(nums) and idx + 1 not in mark:
#                 mark.add(idx+1)
                
#         return score
            
        