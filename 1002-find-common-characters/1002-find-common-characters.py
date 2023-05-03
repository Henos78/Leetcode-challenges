class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = []
        n = len(words)
        dic ={}
        
        #uisng a frequency graph
        for idx, word in enumerate(words):
            for ch in word:
                if ch not in dic:
                    dic[ch] = [0]*n
                    dic[ch][idx] = 1
                else:
                    dic[ch][idx] += 1
        
        for ch in dic:
            for i in range(0, min(dic[ch])):
                res.append(ch)
                
        return res 
        
        
        
        
     