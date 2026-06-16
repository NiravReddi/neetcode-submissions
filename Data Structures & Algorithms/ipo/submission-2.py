class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hash=[]
        intial_w=w
        for i in range(len(profits)):
            heapq.heappush(hash,(-profits[i],capital[i]))
        res=[]
        while(len(res)<k):
            r1=[]
            profit,capital=heapq.heappop(hash)
            while(hash and capital>w):
                heapq.heappush(r1,((profit,capital)))
                profit,capital=heapq.heappop(hash)
            
            if len(hash)==0 and capital>w:
                return w
            res.append(-profit)
            w+= (-profit)
            
            while(r1):
                profit,capital=heapq.heappop(r1)
                heapq.heappush(hash,((profit,capital)))
        print(res)
        return sum(res)+intial_w
                
