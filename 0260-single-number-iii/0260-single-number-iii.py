class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        dic ={}
        
        for num in nums:
            if num not in dic:
                dic[num] =1
            else:
                dic[num] += 1
                
        for num in dic:
            if dic[num] ==1:
                res.append(num)
        
        return res