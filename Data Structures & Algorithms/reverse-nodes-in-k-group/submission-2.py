# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev=None
            while(head!=None):
                nex=head.next
                head.next=prev
                prev=head
                head=nex
            return prev
        def printlist(head):
            while(head!=None):
                print(head.val)
                head=head.next
            
        ret=ListNode(0,head)
        prevassign=ret
        while(head!=None):
            start=head
            deplete=k
            travel=head
            prev=None
            while(deplete>0 and travel!=None):
                prev=travel
                travel=travel.next
                deplete-=1
            if deplete==0:
                prev.next=None
                start=reverse(start)
                end=start
                while(end.next!=None):
                    end=end.next
                end.next=travel
                prevassign.next=start
                prevassign=end
                head=travel
            else:
                head=None
        return ret.next
            