# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            prev=None
            while(head!=None):
                temp=head.next
                head.next=prev
                prev=head
                head=temp
            return prev
        def printlist(head):
            while(head!=None):
                print(head.val)
                head=head.next
            
        ret=ListNode(0,head)
        retheadl=head
        retheadr=head
        prevl=ret
        prevr=ret
        while(left>1):
            prevl=retheadl
            retheadl=retheadl.next
            retheadr=retheadr.next
            left-=1
            right-=1
        while(right>0):
            prevr=retheadr
            retheadr=retheadr.next
            right-=1
        prevr.next=None
        prevl.next=None
        retheadl=reverse(retheadl)
        prevl.next=retheadl
        while(prevl.next!=None):
            prevl=prevl.next
        prevl.next=retheadr
        return ret.next