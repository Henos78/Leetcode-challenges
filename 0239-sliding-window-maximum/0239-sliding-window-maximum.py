class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #solution using monotonitc queue
        res= []
        que = deque()
        
        l =r=0
        
        while r <len(nums):
            while que and nums[que[-1]] < nums[r]:
                que.pop()
            que.append(r)
            
            #to remove the left value from window
            if l > que[0]:
                que.popleft()
            
            if r +1 >=k:
                res.append(nums[que[0]])
                l +=1
                
            r+= 1
            
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
        
        