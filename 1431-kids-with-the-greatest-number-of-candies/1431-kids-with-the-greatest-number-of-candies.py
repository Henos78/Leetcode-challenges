class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res =[]
        k = extraCandies
        
        for i in range(len(candies)):
            candies[i] +=k
            temp = max(candies)
            if candies[i] == temp:
                res.append(True)
            else:
                res.append(False)
            candies[i]-=k
            
        return res
        