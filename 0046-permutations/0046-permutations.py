class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # using bit
    
        res = []
        seen = 0
        
        #temp variable to store or permuutation subsets
        def helper(res,seen,temp):
            if len(temp) == len(nums):
                res.append(temp)
                
            for i in range(len(nums)):
                if not seen &(1<<i):
                    seen |= (1 << i)
                    helper(res,seen,temp+[nums[i]])
                    seen ^= (1 << i)

        helper(res,seen,[])
        
        return res
        