class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[0]*26
        s2=[0]*26
        for i in s:
            s1[97-ord(i)]+=1
        for i in t:
            s2[97-ord(i)]+=1
        if s1==s2:
            return True
        return False
        