class Solution:
    def findComplement(self, num: int) -> int:
        bnum = bin(num)[2:]
        change = "".join(['0' if b == '1' else '1' for b in bnum])
        return int(change,2)
        
        