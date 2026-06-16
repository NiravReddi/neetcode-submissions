class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for i in arr:
            heapq.heappush(heap,(abs(x-i),i))
        res=[]
        while(k>0):
            a,b=heapq.heappop(heap)
            res.append(b)
            k-=1
        return sorted(res)