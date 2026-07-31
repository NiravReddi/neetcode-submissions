class Linkedlist:
        def __init__(self,val,prev=None,next=None):
            self.prev=prev
            self.next=next
            self.val=val
class MyCircularQueue:
    

    def __init__(self, k: int):
        self.cap=k
        self.size=0
        

    def enQueue(self, value: int) -> bool:
        if self.size==0:
            self.head=Linkedlist(value,None,None)
            self.size+=1
            self.head.prev=self.head
            self.head.next=self.head
        elif self.size==self.cap:
            return False
        else:
            newnode=Linkedlist(value,None,None)
            last=self.head.prev
            self.head.prev=newnode
            last.next=newnode
            newnode.next=self.head
            newnode.prev=last
            self.size+=1
        return True
        

    def deQueue(self) -> bool:
        if self.size==0:
            return False
        else:
            last=self.head.prev
            next=self.head.next
            self.head=self.head.next
            next.prev=last
            last.next=next
            self.size-=1
        return True
        

    def Front(self) -> int:
        if self.size==0:
            return -1
        else:
            return self.head.val
        

    def Rear(self) -> int:
        if self.size==0:
            return -1
        else:
            return self.head.prev.val
        

    def isEmpty(self) -> bool:
        return self.size==0
            
        

    def isFull(self) -> bool:
        return self.size==self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()