class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pre = [0]*(len(arr)+1)
        ans= []
        for i in range(len(arr)):
            pre[i]= pre[i-1]^arr[i]
        print(pre)
        
        for que in queries:
            temp =  pre[que[0]-1] ^ pre[que[1]]
            ans.append(temp)
            
        return ans
                
        