class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking solution
        res= []
        temp = []
        
        def backtrack(idx):
            res.append(temp[:])
            for idx in range(idx, len(nums)):
                temp.append(nums[idx])
                backtrack(idx+1)
                temp.pop()
                
        backtrack(0)
        return res
        
        
        
        
        
        # def backtrack(start, end, tmp):
        #     ans.append(tmp[:])
        #     for i in range(start, end):
        #         tmp.append(nums[i])
        #         backtrack(i+1, end, tmp)
        #         tmp.pop()
        # ans = []
        # backtrack(0, len(nums), [])
        # return ans
        