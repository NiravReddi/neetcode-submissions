class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=0
        dic=defaultdict(int)
        for i in range(len(s)):
            if s[i] in dic.keys():
                r=[]
                prev=dic[s[i]]
                for j in dic.keys():
                    if dic[j]<prev:
                        r.append(j)
                for j in r:
                    del dic[j]
                dic[s[i]]=i
            else:
                dic[s[i]]=i
            n=max(n,len(dic.keys()))
        return n