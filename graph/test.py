class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        current=self.root
        for a in word:
            if a not in current:
                current.children[a]=TrieNode()
            current=current.children[a]