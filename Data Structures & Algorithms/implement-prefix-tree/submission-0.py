class TrieNode:
    def __init__(self,char):
        self.char=char
        self.children={}
        self.is_last=False
class PrefixTree:

    def __init__(self):
        self.trie=TrieNode("#")
        

    def insert(self, word: str) -> None:
        root=self.trie

        for i in word:
            if i in root.children.keys():
                root=root.children[i]
            else:
                root.children[i]=TrieNode(i)
                root=root.children[i]
        root.is_last=True


    def search(self, word: str) -> bool:

        root=self.trie

        for i in word:
            if i not in root.children.keys():
                return False
            root=root.children[i]
        
        return root.is_last
        

    def startsWith(self, prefix: str) -> bool:
        root=self.trie

        for i in prefix:
            if i not in root.children.keys():
                return False
            root=root.children[i]
        
        return True
        
        