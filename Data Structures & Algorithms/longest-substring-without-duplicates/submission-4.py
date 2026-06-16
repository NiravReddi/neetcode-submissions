class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=1
        if s=="":
            return 0
        dic=defaultdict(int)
        l=0
        for i in range(len(s)):
            dic[s[i]]+=1
            while(dic[s[i]]>1):
                dic[s[l]]-=1
                l+=1
            res=max(res,i-l+1)
        return res