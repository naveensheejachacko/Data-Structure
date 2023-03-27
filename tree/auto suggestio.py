class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        current=self.root
        for c in word:
            if c not in current.children:
                current.children[c]=TrieNode()
            current=current.children[c]
        current.endOfWord=True
    def search(self,word):
        current=self.root
        for c in word:
            if c not in current.children:
                return False
            current=current.children[c]
        return current.endOfWord
    # def startsWith(self,prefix):
    #     current=self.root
    #     for c in prefix:
    #         if c not in current.children:
    #             return False
    #         current=current.children[c]
    #         return True

    def printAutoSuggestion(self,key):
        current = self.root
        for a in key:
            if a not in current.children:
                return 0
            current =current.children[a]
            # if not current.children:
            #     return -1
        self.suggestionsRec(current, key)
        return 1
    def suggestionsRec(self,current,word):
        if current.endOfWord:
            print(word)
        for a,n in current.children.items():
            self.suggestionsRec(n,word+a)

 
t=Trie()
t.insert('apple')
t.insert('apps')
t.insert('pineapple')
t.insert('pen')
t.insert('ppppp')
# c=t.search('apple')
# print("the search result is:",c)
# s=t.startsWith('app')
# print(s)
key = "a" 
comp = t.printAutoSuggestion(key)
# if comp == -1:
#     print("No other strings found with this prefix\n")
if comp == 0:
    print("No string found with this prefix\n")