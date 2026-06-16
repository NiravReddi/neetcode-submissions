class FreqStack:

    def __init__(self):
        self.stack=[]
        self.dic=defaultdict(int)
        self.ind=0
        

    def push(self, val: int) -> None:
        self.dic[val]+=1
        heapq.heappush(self.stack,(-self.dic[val],-self.ind,val))
        self.ind+=1

        

    def pop(self) -> int:
        freq,index,val=heapq.heappop(self.stack)
        self.dic[val]-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()