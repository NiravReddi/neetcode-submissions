class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        flag=True
        i=0
        j=0
        while(i<len(word1) and j<len(word2)):
            if flag:
                res+=word1[i]
                i+=1
            else:
                res+=word2[j]
                j+=1
            flag= not flag
        while(i<len(word1)):
            res+=word1[i]
            i+=1
        while(j<len(word2)):
            res+=word2[j]
            j+=1
        return res