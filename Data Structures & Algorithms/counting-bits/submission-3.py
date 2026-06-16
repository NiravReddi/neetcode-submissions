class Solution:
    def countBits(self, n: int) -> List[int]:

        ret=[0,1]
        i=1
        while(i<=n):
            r=[]
            for i in ret:
                r.append(1+i)
            i=i*2
            ret.extend(r)
            if len(ret)>n:
                break
        return ret[:n+1]
        