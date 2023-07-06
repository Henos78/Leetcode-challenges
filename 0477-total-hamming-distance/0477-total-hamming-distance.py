class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res =0
        n=len(nums)
        
        #iterate  through evry bit position
        for i in range(32):
            count =0 #keeps track of num in nums which bit is 1 in that  position
            
            for num in nums:
                count += (num>>i)&1
                
            res += count*(n-count) #(n-count) is the val where the bit is 0.
            
        return res
            
        
        """
        #works but tle t.c = o(n^3)
        res = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                temp= nums[i]^nums[j]
                res += sum([int(i) for i in bin(temp)[2:]])
        return res
        """
                

        