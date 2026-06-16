class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        heap=[]
        for i in dic.keys():
            heapq.heappush(heap,(-dic[i],i))
        res=[]
        while(k):
            i,j=heapq.heappop(heap)
            res.append(j)
            k-=1
        return res