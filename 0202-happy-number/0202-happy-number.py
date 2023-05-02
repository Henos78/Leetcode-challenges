class Solution:
    def isHappy(self, n: int) -> bool:
        #do this question again
        def next_num(n):
            s =str(n)
            cal = [ int(i) for i in s]
            for i in range(len(cal)):
                cal[i] = cal[i]*cal[i]
            return sum(cal)
        
        
        seen = set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = next_num(n)
            
        return n == 1
            
           