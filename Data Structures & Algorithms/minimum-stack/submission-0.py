class MinStack:

    def __init__(self):
        self.mn=(2^31)-1
        self.tp=-1
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mn=min(self.mn,val)
        self.tp+=1
        

    def pop(self) -> None:
        self.tp-=1
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[self.tp]
        

    def getMin(self) -> int:
        return min(self.stack)
        
