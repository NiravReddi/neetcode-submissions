class WordDictionary:
    class Trie:
        def __init__(self):
            self.children=[0 for i in range(26)]
            self.ends=False

    def __init__(self):
        self.head=self.Trie()
        

    def addWord(self, word: str) -> None:
        curr=self.head
        for i in word:
            if curr.children[ord(i)-ord('a')]==0:
                newnode=self.Trie()
                curr.children[ord(i)-ord('a')]=newnode
                curr=newnode
            else:
                curr=curr.children[ord(i)-ord('a')]
        curr.ends=True
        

    def search(self, word: str) -> bool:
        curr=self.head
        q=[curr]
        ind=0
        while(q and ind<len(word)):
            r1=[]
            for i in q:
                if word[ind]==".":
                    for k in i.children:
                        if k!=0:
                            r1.append(k)
                else:
                    if i.children[ord(word[ind])-ord('a')] !=0:
                        r1.append(i.children[ord(word[ind])-ord('a')])
            q=r1
            
            if ind==len(word)-1:
                for i in q:
                    if i.ends:
                        return True
                return False
            ind+=1
            
        return False

