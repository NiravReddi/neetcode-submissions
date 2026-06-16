class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def istrue(dic,s):
            rt=defaultdict(int)
            f=0
            for i in s:
                rt[i]+=1
            for i in dic.keys():
                if dic[i]>rt[i]:
                    f=1
            if f==0:
                return True
            return False
        checkdic=defaultdict(int)
        for i in t:
            checkdic[i]+=1
        l=0
        scheck=""
        ret="s"*1001
        for r in range(len(s)):
            scheck+=s[r]
            while(istrue(checkdic,scheck)):
                if len(scheck)<len(ret):
                    ret=scheck
                l+=1
                scheck=s[l:r+1]
        if ret == "s"*1001:
            return ""
        return ret