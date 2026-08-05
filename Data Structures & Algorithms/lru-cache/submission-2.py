class LRUCache:
    class ListNode:
        def __init__(self,val:int,key:int,prev=None,next=None):
            self.val=val
            self.key=key
            self.next=next
            self.prev=prev

    def __init__(self, capacity: int):
        self.cap=capacity
        self.keys={}
        self.head=self.ListNode(0,0)
        self.end=self.ListNode(0,0)
        self.end.prev=self.head
        self.head.next=self.end
    def insert(self,newnode):
        newnode.next=self.head.next
        self.head.next.prev=newnode
        self.head.next=newnode
        
        newnode.prev=self.head
    def delete(self,delnode):
        delnode.prev.next=delnode.next
        delnode.next.prev=delnode.prev
        del self.keys[delnode.key]
        del delnode
        
        
        
        
    def printlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.key,"-------",curr.val)
            curr=curr.next

    def get(self, key: int) -> int:
        if key in self.keys:
            node=self.keys[key]
            nodeval=node.val
            nodekey=key
            self.delete(node)
            newnode=self.ListNode(nodeval,nodekey)
            self.insert(newnode)
            self.keys[key]=newnode
            return nodeval
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.keys:
            print("yay")
            node=self.keys[key]
            nodeval=value
            nodekey=key
            self.delete(node)
            newnode=self.ListNode(nodeval,nodekey)
            self.insert(newnode)
            self.keys[key]=newnode
            
            
        else:

            if len(self.keys)==self.cap:
                self.delete(self.end.prev)
            nodeval=value
            nodekey=key
            newnode=self.ListNode(nodeval,nodekey)
            self.insert(newnode)
            self.keys[key]=newnode
        
            



        
