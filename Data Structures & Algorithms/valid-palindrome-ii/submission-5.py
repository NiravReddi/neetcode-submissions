class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalin(front,back,one):
            if front>=back:
                return True
            if s[front].lower()==s[back].lower():
                return ispalin(front+1,back-1,one)
            else:
                if one:
                    return ispalin(front+1,back,0) or ispalin(front,back-1,0)
                else:
                    return False
        return ispalin(0,len(s)-1,1)
        