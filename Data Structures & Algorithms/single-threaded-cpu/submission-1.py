class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res=[]
        hash=[]
        for i in range(len(tasks)):
            heapq.heappush(hash,(tasks[i][0],tasks[i][1],i))
        
        q=[heapq.heappop(hash)]
        lasttime=0
        while(q):
            r1=[]
            enqueuetime,processtime,index=q.pop()
            res.append(index)
            
                
            if lasttime>=enqueuetime:
                lasttime+=processtime
            else:
                lasttime=enqueuetime+processtime
            while hash and hash[0][0]<=lasttime:
                i,j,k=heapq.heappop(hash)
                heapq.heappush(r1,(j,i,k))
            if r1:
                i,j,k=heapq.heappop(r1)
                q.append((j,i,k))
                while r1:
                    i,j,k=heapq.heappop(r1)
                    heapq.heappush(hash,(j,i,k))

            elif hash:
                i,j,k=heapq.heappop(hash)
                q.append((i,j,k))
        



        return res
