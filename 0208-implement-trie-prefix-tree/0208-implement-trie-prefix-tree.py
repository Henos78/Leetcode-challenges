# Here we are using an array to build our trie tree
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        
        for ch in word:
            i = ord(ch)-ord("a")
        
            if cur.children[i] == None: 
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        
        cur.end = True  

    def search(self, word: str) -> bool:
        cur = self.root
        
        for ch in word:
            i = ord(ch)-ord("a")
            if cur.children[i]== None:
                return False
            cur = cur.children[i]
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for ch in prefix:
            i = ord(ch)-ord("a")
            if cur.children[i]==None:
                return False
            cur = cur.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)