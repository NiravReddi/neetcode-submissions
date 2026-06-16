class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=0
        l=0
        dic=defaultdict(int)
        for r in range(len(s)):
            dic[s[r]]=1+dic[s[r]]

            n=max(n,dic[s[r]])

            if (r-l+1)-n >k:
                dic[s[l]]-=1
                l+=1
            
        return (r-l+1)