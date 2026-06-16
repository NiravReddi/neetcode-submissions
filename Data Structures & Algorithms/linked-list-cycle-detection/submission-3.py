# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head.next
        slow=head
        while(fast!=None and slow!=None):
            if fast.next!=None:
                fast=fast.next.next
            else:
                fast=fast.next
            slow=slow.next
            if fast==slow:
                return True
        return False
