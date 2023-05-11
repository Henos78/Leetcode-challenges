class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxheap = []
        
        if a > 0:
            heapq.heappush(maxheap,(-a, 'a'))
        if b >0:
            heapq.heappush(maxheap,(-b, 'b'))
        if c > 0:
            heapq.heappush(maxheap,(-c, 'c'))
                
        while maxheap:
            num, ch = heapq.heappop(maxheap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if len(maxheap) == 0:
                    break
                    
                num2, ch2 = heapq.heappop(maxheap)
                res += ch2
                num2 += 1
                
                if num2:
                    heapq.heappush(maxheap, (num2, ch2))    
            else:
                res += ch
                num += 1   
                
            if num:
                heapq.heappush(maxheap, (num, ch))
                
        return res 
            
    
        """
    # Frist trail (wrong submission)
     while maxheap:
            val, ch = heapq.heappop(maxheap)
            #to. find the highest character
            if not res or res[-1] != ch:
                if val <-1:
                    res += ch*2
                    heapq.heappush(maxheap, (val +2, ch))
                else:
                    res += ch
                    
            else:
                # to find the second highest character
                if not maxheap:
                    break
                    
                val1, ch1 = heapq.heappop(maxheap)
                if val1 <-1:
                    res += ch1*2
                    heapq.heappush(maxheap,(val1+2, ch))
                else:
                    res += ch1
                    
                heapq.heappush(maxheap,(val,ch))
            
        return res
    

                    
        
    
        """
   