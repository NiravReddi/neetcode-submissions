import bisect
class MedianFinder:

    def __init__(self):
        self.heap=[]
        self.cap=0
        

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.heap,num)
        self.cap+=1

    def findMedian(self) -> float:
        print(self.cap,self.heap)
        if self.cap%2 ==0:
            mid=self.cap//2
            res=heapq.nsmallest(mid+1,self.heap)
            
            return (res[-1]+res[-2])/2
        else:
            mid=math.floor(self.cap/2)
            
            return self.heap[mid]
        
        