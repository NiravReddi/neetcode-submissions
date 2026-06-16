class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        r=[]
        for i in strs:
            dic={}
            for j in i:
                if j not in dic.keys():
                    dic[j]=1
                else:
                    dic[j]+=1
            a.append(dic)
        while(len(strs)>0 and len(a)>0):
            r.append([strs.pop(0)])
            comp=a.pop(0)
            j=0
            while(j<len(a)):
                if a[j]==comp:
                    r[len(r)-1].append(strs.pop(j))
                    a.pop(j)
                else:
                    j+=1
        return r
