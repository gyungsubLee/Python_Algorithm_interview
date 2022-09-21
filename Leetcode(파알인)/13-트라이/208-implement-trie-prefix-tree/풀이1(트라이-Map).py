# Reference)
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/2067181/Clean-and-Concise-Python-Solution-with-Comments-Easy-to-Understand

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root                        
        for c in word:                        
            if c not in cur.children:         
                cur.children[c] = TrieNode() 
            cur = cur.children[c]             
        cur.endOfWord = True          

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False         
            cur = cur.children[c]  
        return cur.endOfWord
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

a = Trie()

a.insert('apple')
a.search('apple') # True
a.search('app') # False
a.startsWith('app') # True
a.insert('app') 
a.search('app') # True