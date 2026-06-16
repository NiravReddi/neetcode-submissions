class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s[:])
        for i in t:
            if i in a:
                a.remove(i)
            else:
                return False
        if len(a)==0:
            return True
        return False
        