
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        #attempt two using dfs and memorization in short only
        memo ={}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            start = 0
            for ch in word:
                start = s.find(ch,start)+1
                if not start:
                    memo[word] = False
                    return False
            
            memo[word] = True
            return True
        
        return sum(dfs(word) for word in words)
            
    
        
        