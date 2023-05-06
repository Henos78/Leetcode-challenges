class Solution:
    def specialArray(self, nums: List[int]) -> int:
        #Solving using binary search
          
        n = len(nums)
        l,r =0, n
        
        while l<=r:
            mid = (l+r)//2
            ans = 0
            
            for num in nums:
                if num >= mid:
                    ans +=1
                    
            if ans == mid:
                return mid
            elif ans >mid:
                l = mid +1
            else:
                r = mid -1
                
        return -1
            
        
        
        
       