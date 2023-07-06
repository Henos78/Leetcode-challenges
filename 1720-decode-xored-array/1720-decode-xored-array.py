class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [0]*(len(encoded)+1)
        res[0]=first
        print(6^4)
        
        for i in range(1,len(encoded)+1):
            res[i] = encoded[i-1]^res[i-1]
        
        return res