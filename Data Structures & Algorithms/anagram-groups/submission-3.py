class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makekey(st):
            dic={}
            for i in st:
                if i in dic.keys():
                    dic[i]+=1
                else:
                    dic[i]=1
            res=""
            for i in sorted(dic.keys()):
                res+=i+str(dic[i])
            return res
        resdic={}
        for i in strs:
            key=makekey(i)
            if key in resdic.keys():
                resdic[key].append(i)
            else:
                resdic[key]=[i]
        res=[]
        for i in resdic.keys():
            res.append(resdic[i])
        return res