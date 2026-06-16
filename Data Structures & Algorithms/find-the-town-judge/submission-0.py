class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted={}
        revtrust={}
        for i,j in trust:
            if j in trusted.keys():
                if i not in trusted[j]:
                    trusted[j].append(i)
            else:
                trusted[j]=[i]
            if i in revtrust.keys():
                revtrust[i].append(j)
            else:
                revtrust[i]=[j]
        for j in trusted.keys():
            if len(trusted[j])==n-1 and j not in revtrust.keys():
                return j
        return -1 
        