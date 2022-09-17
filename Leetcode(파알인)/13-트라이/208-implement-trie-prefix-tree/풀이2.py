# Reference) 
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/631419/Python-sol-by-dictionary.-80%2B-w-Visualization

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        table = self.trie
        for char in word:
            if char not in table:
                table[char] = {}
            table = table[char]
        table['@'] = {}
        
    def search(self, word: str) -> bool:
        table = self.trie
        for char in word:
            table = table.get(char, None)
            if table is None:
                return False
        return ( '@' in table )
        
    def startsWith(self, prefix: str) -> bool:
        table = self.trie
        for char in prefix:
            table = table.get(char, None)
            if table is None:
                return False
        return True

a = Trie()

a.insert('apple')
a.search('apple') # True
a.search('app') # False
a.startsWith('app') # True
a.insert('app') 
a.search('app') # True