class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            temp=nums[i]
            for j in range(i,len(nums)):
                temp = lcm(nums[j],temp)
                if temp==k:
                    count +=1
                elif temp>k:
                    break

        return count
        