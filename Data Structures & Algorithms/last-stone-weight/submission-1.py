class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        while(len(heap)>1):
            res1=heapq.heappop(heap)
            res2=heapq.heappop(heap)
            if res1==res2:
                continue
            elif -res1>-res2:
                heapq.heappush(heap,-((-res1)-(-res2)))
        if len(heap)==0:
            return 0
        return -heap[0]

        