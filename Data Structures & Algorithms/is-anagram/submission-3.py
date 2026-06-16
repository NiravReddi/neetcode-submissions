class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def makedict(st):
            dic={}
            for i in st:
                if i in dic.keys():
                    dic[i]+=1
                else:
                    dic[i]=1
            return dic
        return makedict(s)==makedict(t)