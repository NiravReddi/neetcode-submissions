class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        dic={}
        res=0
        for r in range(len(s)):
            while s[r] in dic.keys():
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    del dic[s[l]]
                l+=1
            dic[s[r]]=1
            res=max(res,r-l+1)
        return res