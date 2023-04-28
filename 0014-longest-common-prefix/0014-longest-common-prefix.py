class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Using Tries
        self.add(strs)
        return self.longest()
        
    def __init__(self):
            self.root = TrieNode()
            
    def add(self, strs):

        for s in strs:
            cur = self.root
            for i in s:
                if i not in cur.children:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
                
            cur.end = True
            
    def longest(self):
        cur = self.root
        res= ""
        
        while len(cur.children) ==1 and cur.end == False:
            temp = list(cur.children.keys())[0]
            res += temp
            cur = cur.children[temp]
            
        return res
            
    
        
        