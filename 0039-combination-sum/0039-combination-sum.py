class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res =[]
        
        def backtrack(i,temp,total):
            
            if total == target:
                res.append(temp.copy())
                return
            if i >=len(candidates) or total>target:
                return
            
            temp.append(candidates[i])
            backtrack(i,temp,total+candidates[i])
            temp.pop()
            backtrack(i+1,temp, total)
            
        backtrack(0,[],0)
        return res
        
            
        