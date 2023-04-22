class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        #brute force appraoch 
        banned = set(banned)
        count = 0
        temp = 0

        
        for i in range(1, n+1):
            if i not in banned:
                if temp + i <= maxSum:
                    temp += i
                    count +=1
                    
        return count
            
                
        