class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i,j in points:
            heapq.heappush(heap,(math.sqrt(((-i)**2)+((-j)**2)),i,j))
        res=heapq.nsmallest(k,heap)
        ret=[]
        for i in range(k):
            ret.append([res[i][1],res[i][2]])
        return ret