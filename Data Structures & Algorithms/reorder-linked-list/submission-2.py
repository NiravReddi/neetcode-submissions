# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while(fast!=None):
            if fast.next!=None:
                fast=fast.next.next
            else:
                fast=fast.next
                break
            slow=slow.next
        def rev(head):
            prev=None
            curr=head
            while(curr!=None):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        head2=slow.next
        slow.next=None
        slow=rev(head2)
        ret=head
        while(head is not None and slow is not None):
            temp=head.next
            head.next=slow
            slow=slow.next
            head.next.next=temp
            head=temp
        