class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #solution based on the given hint
        
        if len(nums)<=4:
            return 0
        
        nums.sort()
        a =nums[-1]-nums[3]
        b = nums[-2] -nums[2]
        c=  nums[-3]-nums[1]
        d = nums[-4]- nums[0]
        
        return min(a,b,c,d)
        
        
        """
        #first approach (doesnt work fully)
        minarr, maxarr = nums[:], nums[:]
        for i in range(3):
            minarr.sort()
            temp = min(minarr)
            minarr[-1] = temp
        
        for i in range(3):
            maxarr.sort()
            temp = max(maxarr)
            maxarr[0] = temp
        
        a =max(minarr)-min(minarr)
        b = max(maxarr)-min(maxarr)
        c = max(nums)-min(nums)
        
        return (min(a,b,c))
        """
            
            
            
            
        