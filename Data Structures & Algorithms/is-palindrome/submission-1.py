class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)-1
        i=0
        j=len(s)-1
        while(i<n//2+1):
            print(s[i],s[j])
            if s[i].isalnum() == False:
                i+=1
                continue
            elif s[j].isalnum() == False:
                j-=1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True