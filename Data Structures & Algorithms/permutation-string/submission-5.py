class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dics1={}
        for i in s1:
            if i in dics1.keys():
                dics1[i]+=1
            else:
                dics1[i]=1
        def checkprem(s):
            dic={}
            for i in s:
                if i in dic.keys():
                    dic[i]+=1
                else:
                    dic[i]=1
            return dic==dics1
        for i in range(0,len(s2)-len(s1)+1):
            if checkprem(s2[i:i+len(s1)]):
                return True
        return False