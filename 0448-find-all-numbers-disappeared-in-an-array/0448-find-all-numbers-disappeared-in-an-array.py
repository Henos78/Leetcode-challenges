class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # different appraoch using extra space
        n = len(nums)
        nums = set(nums)
        
        res = set(range(1,n+1)) - nums
        
        return list(res)
       
                
               
        """
            #brute force approach tle
            n= len(nums)
            res = []

            for  i in range(1,n+1):
                if i not in nums:
                    res.append(i)

            return res

     """

        