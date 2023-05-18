class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxpro= 0
        temp = [0]*len(words)
        
        for i in range(len(words)):
            for ch in words[i]:
                temp[i] |= 1 << (ord(ch)-ord('a'))

     
        for i in range(len(words)):
            for j in range(1, len(words)):
                if temp[i]&temp[j] == 0:
                    pro= len(words[i])*len(words[j])
                    maxpro = max(pro,maxpro)
        return maxpro
            