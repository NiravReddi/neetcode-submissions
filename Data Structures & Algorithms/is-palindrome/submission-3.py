class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i.isalnum():
                st+=i.lower()
        mid=len(st)//2
        for i in range(mid):
            if st[i]!=st[len(st)-i-1]:
                return False
        return True
        