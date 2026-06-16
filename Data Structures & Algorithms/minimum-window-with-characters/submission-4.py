class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic=defaultdict(int)
        for i in t:
            dic[i]+=1
        def check(st):
            dic1=defaultdict(int)
            for i in st:
                dic1[i]+=1
            for i in dic.keys():
                if i not in dic1.keys() or dic[i]>dic1[i]:
                    return False
            
            return True
        curr=s[0]
        res="s"*1001
        l=0
        if check(curr):
            if len(curr)<len(res):
                res=curr
        
        for r in range(1,len(s)):
            curr+=s[r]
            while(check(curr)):
                if len(curr)<len(res):
                    res=curr
                l+=1
                curr=curr[1:]
        if res=="s"*1001:
            return ""
        return res


        