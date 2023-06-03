class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        res =0
        
        even,odd = [],[]
        for  i in range(len(nums)):
            if nums[i]%2 ==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        j,k=0,0 # j-even idx, k-odd idx
        for  i in range(len(target)):
            if target[i] %2 ==0:
                res += abs(target[i]-even[j]) //2
                j +=1
            else:
                res += abs(target[i]-odd[k]) //2
                k +=1
                
        return res //2 #each pair  is being calculated once so we divide our res by 2
            
        
          
                
        
            