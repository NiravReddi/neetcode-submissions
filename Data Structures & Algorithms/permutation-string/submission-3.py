class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1=defaultdict(int)
        for i in s1:
            dic1[i]+=1
        dic2=defaultdict(int)
        l=0
        dic2[s2[0]]+=1
        if dic2==dic1:
            return True
        for r in range(1,len(s2)):
            dic2[s2[r]]+=1
            if r-l+1 == len(s1):
                if dic2==dic1:
                    return True
                dic2[s2[l]]-=1
                if dic2[s2[l]]==0:
                    del dic2[s2[l]]
                l+=1
        return False
