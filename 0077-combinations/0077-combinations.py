class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #using backtracking
        res = []
        comb= []
        
        def backtrack(idx):
            if len(comb)==k:
                res.append(comb[:])
                return
            
            for idx in range(idx, n+1):
                comb.append(idx)
                backtrack(idx+1)
                comb.pop()
                
        backtrack(1)
        return res 
        