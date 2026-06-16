class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        res=[[] for i in range(n)]
        meetings.sort()
        for k,j in meetings:
            flag=True
            ind=0
            leastmindend=100001
            ei=-1
            for i in res:
                ei+=1
                if i!=[]:
                    if i[-1][1]>=k:
                        if leastmindend>i[-1][1]:
                            leastmindend=i[-1][1]
                            ind=ei
                        continue
                    else:
                        i.append([k,j])
                        flag=False
                        break
                else:
                    i.append([k,j])
                    flag=False
                    break
            if flag:
                newstart=res[ind][-1][1]
                newend=(newstart+(j-k))
                res[ind].append([newstart,newend])
                flag=False
        ret=0
        mx=len(res[0])
        for i in range(1,len(res)):
            if len(res[i])>mx:
                mx=len(res[i])
                ret=i
        return ret