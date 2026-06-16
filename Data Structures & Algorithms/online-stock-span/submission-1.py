class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.ind=0
        

    def next(self, price: int) -> int:
        self.ind+=1
        if len(self.stack)==0 or self.stack[-1][0]>price:
            self.stack.append((price,self.ind))
            return 1
        while(self.stack and self.stack[-1][0]<=price):
            lastval,lastind=self.stack.pop()
        self.stack.append((price,lastind))
        return self.ind-lastind+1
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)