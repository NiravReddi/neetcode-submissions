class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
            heapq.heappush(heap,(-count[i],i))
        res=set()
        while(len(res)<k):
            res.add(heapq.heappop(heap)[1])
        return list(res)
        