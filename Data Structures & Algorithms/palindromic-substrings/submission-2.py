class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        def ispalindrome(st):
            return st[::]==st[-1::-1]
        def dfs(l,r):
            nonlocal res
            if l<0 or r>=len(s):
                return
            if ispalindrome(s[l:r+1]):
                res+=1
            dfs(l-1,r+1)
        for i in range(len(s)):
            dfs(i,i)
            dfs(i,i+1)
        return res