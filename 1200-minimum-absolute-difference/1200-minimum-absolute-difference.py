class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = float("inf")
        res = []
        l,r =0,1
        
        while r<len(arr):
            mindiff = min(mindiff, abs(arr[l]-arr[r]))
        
            l +=1
            r +=1
            
        for i in range(1,len(arr)):
            temp = abs(arr[i]-arr[i-1])
            if  mindiff == temp:
                res.append([arr[i-1],arr[i]])
        
        return res