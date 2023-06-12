class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        i=0
        
        while i<len(nums)-1:
            if nums[i]+1!=nums[i+1]:
                res.append(str(nums[i]))
            else:
                temp=nums[i]
                while(i<len(nums)-1 and nums[i]+1==nums[i+1]):
                    i+=1
                temp2=nums[i]
                t=str(temp)+"->"+str(temp2)
                res.append(t)
            i+=1
            
        if i==len(nums)-1:
            res.append(str(nums[len(nums)-1]))
        return res
        
                
            
            
                
                
        