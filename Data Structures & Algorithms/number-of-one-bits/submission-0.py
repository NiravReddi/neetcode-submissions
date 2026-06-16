class Solution:
    def hammingWeight(self, n: int) -> int:

        r=0

        while(n>0):
            if n%2==1:
                r+=1
            n//=2
        return r
        