class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res= []
        n = len(nums)
        
        dic = {}
        
        for num in nums:
            for i in num:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] +=1
                    
        for val in dic:
            if dic[val] == n:
                res.append(val)
                
        res = sorted(res)
        return res
        