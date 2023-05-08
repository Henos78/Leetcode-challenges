class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #We can solve the question using quick sort and bucket sort for now the simpler and most efficiecnt one
        l,r = 0,len(nums)-1
        i = 0
        #to make things easier we will create a function swap
        
        def swap(i,j):
            temp = nums[i]
            nums[i]= nums[j]
            nums[j]= temp
            
        while i<=r:
            if nums[i] == 0:
                swap(l,i)
                l+=1
            elif nums[i] ==2:
                swap(i,r)
                r -=1 
                i -= 1
            i +=1
        