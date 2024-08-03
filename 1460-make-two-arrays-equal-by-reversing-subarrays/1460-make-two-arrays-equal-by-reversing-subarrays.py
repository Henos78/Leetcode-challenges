class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if sorted(target)== sorted(arr):
            return True
        
        target.sort()
        arr.sort()
        n= len(arr)
        
        for  i in range(n):
            if arr[i] !=target[i]:
                return False
        
        return True
        