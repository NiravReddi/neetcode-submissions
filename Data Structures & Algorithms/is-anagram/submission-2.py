class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sana=[0 for i in range(26)]
        tana=[0 for i in range(26)]
        for i in s:
            sana[ord(i)-ord('a')]+=1
        for i in t:
            tana[ord(i)-ord('a')]+=1
        return sana==tana