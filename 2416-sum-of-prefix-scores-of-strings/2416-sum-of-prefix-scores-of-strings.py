class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
        self.visit = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.add(words)
        res = []
        for word in words:
            res.append(self.score(word))
        return res
        
    def __init__(self):
        self.root = Trie()
        
     # we have created our trie node and we are adding the values into the node
    def add (self,words):
        
        for word in words:
            cur = self.root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Trie()
                cur = cur.children[ch]
                cur.visit += 1
                
            cur.end = True
     # this function calculates the pre fix score for the word in words       
    def score(self, word):
        cur = self.root
        pre_sum = 0
        
        for ch in word:
            if ch not in cur.children:
                return pre_sum
            cur = cur.children[ch]
            pre_sum += cur.visit
            
        return pre_sum
    """
    t.c: o(n*m) where n-len of words and m- len of word in words
    worst case at times it might be o(nm^2)
    
    """        
            
        
        
            
            
        