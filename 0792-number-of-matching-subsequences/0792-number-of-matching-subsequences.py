class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True
        
    def find(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end

class Solution:
   
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    
        ans = 0
        trie = Trie()
        seen = {}
        
        for word in words:
            trie.add(word)
            
        for word in words:
            if word not in seen:
                temp = trie.find(word)
                seen[word] = temp and self.dfs(s, word, 0, 0)
                
            if seen[word]:
                ans += 1
                
        return ans
    
    def dfs(self, s, word, i, j):
        if j == len(word):
            return True
        if i == len(s):
            return False
        
        if s[i] == word[j]:
            return self.dfs(s, word, i+1, j+1)
        
        return self.dfs(s, word, i+1, j)

        
        