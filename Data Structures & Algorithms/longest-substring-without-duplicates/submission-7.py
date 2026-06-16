class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        res=0
        for r,val in enumerate(s):
            if s[r] in dic.keys():
                while(s[r] in dic.keys()):
                    del dic[s[l]]
                    l+=1
                dic[s[r]]=1
            else:
                dic[s[r]]=1
            res=max(res,len(dic))
        res=max(res,len(dic))
        return res
