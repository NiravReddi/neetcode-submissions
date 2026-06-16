class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dic={}
        if len(s1)>len(s2):
            return False
        for i in s1:
            if i in s1dic.keys():
                s1dic[i]+=1
            else:
                s1dic[i]=1
        s1len=len(s1)
        s2dic={}
        l=0
        for r in range(s1len):
            if s2[r] in s2dic.keys():
                s2dic[s2[r]]+=1
            else:
                s2dic[s2[r]]=1
        print(s1dic,s2dic)
        if s1dic==s2dic:
            return True
        for r in range(s1len,len(s2)):
            if s2[r] in s2dic.keys():
                s2dic[s2[r]]+=1
            else:
                s2dic[s2[r]]=1
            s2dic[s2[l]]-=1
            if s2dic[s2[l]]==0:
                del s2dic[s2[l]]
            l+=1
            if s1dic==s2dic:
                
                return True
        return False