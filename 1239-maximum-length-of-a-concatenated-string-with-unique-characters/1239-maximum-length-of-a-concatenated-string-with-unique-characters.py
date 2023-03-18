class Solution:
    def maxLength(self, arr: List[str]) -> int:
            self.ans = 0
            def backtrack(i, path):
                cur = "".join(path)
                if len(cur) !=  len(set(cur)):
                    return
                
                self.ans= max(self.ans, len(cur))
                
                if i >= len(arr):
                    return 
                backtrack(i+1, path +[arr[i]])
                backtrack(i+1,path)
                
            backtrack(0,[])  
            return self.ans
            
