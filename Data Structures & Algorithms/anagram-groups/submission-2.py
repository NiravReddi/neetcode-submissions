class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        def makekey(st):
            s=[0 for i in range(26)]
            for k in st:
                s[ord(k)-ord('a')]+=1
            return s
        for i in strs:
            if tuple(makekey(i)) in dic.keys():
                dic[tuple(makekey(i))].append(i)
            else:
                dic[tuple(makekey(i))]=[i]
        res=[]
        for key in dic.keys():
            res.append(dic[key])
        return res