class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key =lambda x:x[1])
        last = float("-inf")
        res = 0
        
        for start, end in  intervals:
            if start < last:
                res  +=1
            else:
                last = end
                
        return res