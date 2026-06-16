class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(st):
            mid=len(st)//2
            for i in range(mid):
                if st[i]!=st[len(st)-i-1]:
                    return False
            return True
        if ispalindrome(s):
            return True
        for i in range(len(s)):
            if ispalindrome(s[:i]+s[i+1:]):
                return True
        return False
        