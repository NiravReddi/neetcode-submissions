class MyCircularQueue:
    class ListNode:
        def __init__(self,val: int,next=None):
            self.val=val
            self.next=next
    def __init__(self, k: int):
        self.head=self.ListNode(0,None)
        self.tail=self.ListNode(0,None)
        self.head.next=self.tail
        self.tail.next=self.head
        self.cap=k
        self.current_size=0
        
        

    def enQueue(self, value: int) -> bool:
        if self.current_size==self.cap:
            return False
        else:
            newnode=self.ListNode(value,None)
            newnode.next=self.tail
            curr=self.head
            while(curr.next!=self.tail):
                curr=curr.next
            curr.next=newnode
            self.current_size+=1
            return True


    def deQueue(self) -> bool:
        if self.current_size==0:
            return False
        else:
            deleteval=self.head.next
            self.head.next=self.head.next.next
            del deleteval
            self.current_size-=1
            return True
        

    def Front(self) -> int:
        if self.current_size==0:
            return -1
        else:
            return self.head.next.val
        

    def Rear(self) -> int:
        if self.current_size==0:
            return -1
        else:
            curr=self.head
            while(curr.next!=self.tail):
                curr=curr.next
            return curr.val
        

    def isEmpty(self) -> bool:
        if self.current_size==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.current_size==self.cap:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()