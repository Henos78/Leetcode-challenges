class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minarr = [0]*len(nums)
        maxarr = [0]*len(nums)
        minarr[0], maxarr[-1]= nums[0], nums[-1]
        
        for i in range(1, len(nums)): #find all  the min values at each index within a range
            minarr[i] = min(nums[i],minarr[i-1])
        
        for i in range(len(nums)-2,-1,-1): #find all max values at each index within a range
            maxarr[i]=max(nums[i],maxarr[i+1])
            
        for i in range(1,len(nums)):
            if nums[i]>minarr[i] and nums[i] < maxarr[i]:
                return True
            
        return False
            
            
        
        
        

        """
        #second approach TLE
        for i in range(1,len(nums)-1):
            temp = max(nums[i+1:])
            temp2 = min(nums[:i])
            
            if temp > nums[i] and temp2< nums[i]:
                return True
        
        return False
            
        #first approach didnt work
        i,j,k=0,1,2
    
        
        while k <=len(nums)-1:
            if nums[i] <nums[j]<nums[k]:
                return True
            i+=1
            j+=1 
            k+=1
            
        return False
        [1,2,0,0,1]
        """