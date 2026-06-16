# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=None
        while(head!=None):
            nex=head.next
            head.next=curr
            curr=head
            head=nex
        return curr
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        ret=head
        ind=0
        prev=None
        while(fast!=None):
            prev=slow
            slow=slow.next
            fast=fast.next
            ind+=1
            if fast!=None:
                fast=fast.next
                ind+=1
        prev.next=None
        newstart=self.reverseList(slow)
        while(newstart!=None):
            temp=ret.next
            ret.next=newstart
            ntemp=newstart.next
            newstart.next=temp
            newstart=ntemp
            ret=temp
        