class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse =True)
    
        res =0
        
        for i in range(0, len(cost),3):
            res += cost[i]
            if i!= len(cost)-1:
                res +=cost[i+1]
                
        return res
            