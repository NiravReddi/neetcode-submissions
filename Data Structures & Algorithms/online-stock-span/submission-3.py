class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.ind=-1
        

    def next(self, price: int) -> int:
        nlastind=self.ind
        self.ind+=1
        while(self.stack and price>=self.stack[-1][0]):
            lastval,lastind=self.stack.pop()
            nlastind=min(lastind,nlastind)
        self.stack.append((price,nlastind))
        return self.ind-nlastind
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)