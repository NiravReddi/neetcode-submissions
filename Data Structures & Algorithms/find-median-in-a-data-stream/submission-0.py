import heapq
class MedianFinder:

    def __init__(self):
        self.n=0
        self.arr=[]

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr,num)
        self.n+=1
        

    def findMedian(self) -> float:
        if self.n%2 == 0:
            k=self.n//2
            return sum(heapq.nlargest(k+1,self.arr)[k-1:k+1])/2
        else:
            k=self.n//2
            return heapq.nlargest(k+1,self.arr)[k]
        
        