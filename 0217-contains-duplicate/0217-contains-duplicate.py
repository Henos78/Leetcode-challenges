class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dic = {}
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] +=1
                
        for val in dic:
            if dic[val] >1:
                return True
            
        return False