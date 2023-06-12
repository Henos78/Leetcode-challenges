class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxx,minn=max(nums),min(nums)
        mul =  maxx*minn # the multiplication of the max and min
        res= []
        for i in range(1,mul+1):
            if maxx%i==0 and minn%i==0:
                res.append(i)
        return max(res)
        
        """
        return gcd(min(nums),max(nums)) #oneliner using built in function
        """
    
        
        