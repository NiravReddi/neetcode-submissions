class MinStack:

    def __init__(self):
        self.mn=[]
        self.tp=-1
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mn)!=0:
            self.mn.append(min(self.mn[self.tp],val))
        else:
            self.mn.append(val)
        self.tp+=1
        

    def pop(self) -> None:
        self.tp-=1
        self.stack.pop()
        self.mn.pop()
        

    def top(self) -> int:
        return self.stack[self.tp]
        

    def getMin(self) -> int:
        print(self.mn,self.stack)
        return self.mn[self.tp]
        
