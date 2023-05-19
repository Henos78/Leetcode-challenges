class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # using recursion /Backtracking solution 
        
        res= []
        
        #basecase
        if len(nums)==1:
            return [nums[:]] # or we can use [nums.copy()]

        for i in range(len(nums)):
            temp = nums.pop(0)
            perm = self.permute(nums)

            for per in perm:
                per.append(temp)
            res.extend(perm)
            nums.append(temp)

        return res
            