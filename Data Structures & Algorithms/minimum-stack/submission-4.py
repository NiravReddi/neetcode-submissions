class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        if self.stack:
            mn=min(val,self.stack[-1][1])
        else:
            mn=val
        self.stack.append((val,mn))
        

    def pop(self) -> None:
        return self.stack.pop()[1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
