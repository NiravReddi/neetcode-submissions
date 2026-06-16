class TrieNode:

    def __init__(self,char):
        self.char=char
        self.children={}
        self.is_last=False

class WordDictionary:

    def __init__(self):
        self.trie=TrieNode("#")
        

    def addWord(self, word: str) -> None:
        root=self.trie

        for i in word:
            if i not in root.children.keys():
                root.children[i]=TrieNode(i)
            root=root.children[i]
        
        root.is_last=True
        

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_last

        return dfs(0, self.trie)
