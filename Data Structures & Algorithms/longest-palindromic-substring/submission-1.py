class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        def ispalindrome(st):
            return st[::]==st[-1::-1]
        def dfs(l,r):
            
            nonlocal res,resLen
            if l<0 or r>=len(s):
                return
            if ispalindrome(s[l:r+1]) and resLen<(r-l+1):
                
                res=s[l:r+1]
                resLen=(r-l+1)
            dfs(l-1,r+1)
        for i in range(len(s)):
            dfs(i,i)
            dfs(i,i+1)
        return res
            
