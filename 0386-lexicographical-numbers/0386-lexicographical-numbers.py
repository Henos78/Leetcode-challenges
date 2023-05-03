class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Do it all over again on your own
        
        # Define a TrieNode class
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False
        
        # Insert a number into the Trie
        def add(num, node):
            for ch in str(num):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        def dfs(node, prefix, res):
            if node.is_end:
                res.append(int(prefix))
            for ch in node.children:
                dfs(node.children[ch], prefix + ch, res)
        
        # add the number to the trie
        root = TrieNode()
        for i in range(1, n+1):
            add(i, root)
        
        res = []
        dfs(root, "", res)
        return res
