# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret=ListNode(0,None)
        head=ret
        while(list1!=None and list2!=None):
            if list1.val<=list2.val:
                ret.next=list1
                ret=ret.next
                list1=list1.next
            else:
                ret.next=list2
                ret=ret.next
                list2=list2.next
        while(list1!=None):
            ret.next=list1
            ret=ret.next
            list1=list1.next
        while(list2!=None):
            ret.next=list2
            ret=ret.next
            list2=list2.next
        return head.next