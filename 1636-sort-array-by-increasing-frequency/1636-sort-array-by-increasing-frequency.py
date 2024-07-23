class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq= Counter(nums)
        print(freq)
        
        nums.sort(key=lambda x: (freq[x], -x))
        return nums

        
       
        
            
        