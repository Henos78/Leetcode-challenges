class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        n=len(nums)
        for i in range(2 ** n):
            subset = []
            for j in range(n):
                if i >> j & 1:
                    subset.append(nums[j])
            res.append(subset)
            
        print(3|2|1|5)
        max_or = 0
        
        for sub in nums:
            max_or|=sub
        
        count =0
        for sub in res:
            temp = 0
            for i in sub:
                temp|=i
            if temp == max_or:
                count+=1
        
        return count
                
        