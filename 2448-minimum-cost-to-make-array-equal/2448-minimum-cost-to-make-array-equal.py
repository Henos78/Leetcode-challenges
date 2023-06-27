class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        #second trial(do it again using different appraoch)
        
        pairs=sorted(list(zip(nums,cost)))
        midCost=sum(cost)/2
        tempCost =0
        
        for n,c in pairs:
            tempCost+=c
            if tempCost>=midCost:
                f=n
                break

        res =0
        for n,c in pairs:
            res+=abs(n-f)*c

        return res 
        """
        #wrong approach and wrong answer
        n=len(nums)
        res=[0]*n
        
        i = 0
        
        while i<n:
            temp = nums[i]
            
            for j in range(n):
                if nums[j] != temp:
                    res[i] += abs(nums[j]-temp)
            i+=1
        print(res)  
        return min(res)
        """