class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [i for i in range(1,len(nums)+1)]
        dic = Counter(nums)
        res = []
        
        for val in dic:
            if dic[val] >1:
                res.append(val)
                
        for val in arr:
            if val not in nums:
                res.append(val)
        
        return res
        