class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        #optimzed solution t.c: o(nlogn)
        
        def digit_sum(n):
            return sum(map(int,str(n)))
        
        
        sumi = defaultdict(list)
        res = -1
        for i, num in enumerate(nums):
            temp = digit_sum(num)
            if temp in sumi:
                res = max(res, num - sumi[temp][0])
            heapq.heappush(sumi[temp], -num)
            
            
        return res
    
    """
    #brute force t.c: o(n^2*k)
        def digit_sum(n):
            return sum(map(int,str(n)))
        
        sumi = []
        res = -1
        for i in range(len(nums)):
            temp = list(str(nums[i]))
            temp = list(map(int,temp))
            sumi.append(sum(temp))
            
             (or we can simple use:
             sumi.append(digit_sum(nums[i])))
        
        for i in range(len(sumi)):
            for j in range(i+1, len(sumi)):
                if sumi[i] == sumi[j]:
                    res = max(res, nums[i] +nums[j])
                    
        return res
    """