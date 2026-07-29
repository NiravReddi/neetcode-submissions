# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        ret=ListNode(0,None)
        retur=ret

        while(l1!=None and l2!=None):
            newval=l1.val+l2.val+c
            c=newval//10
            newval=newval%10
            temp=ListNode(newval,None)
            ret.next=temp
            ret=ret.next
            l1=l1.next
            l2=l2.next
        while(l1!=None):
            newval=l1.val+c
            c=newval//10
            newval=newval%10
            temp=ListNode(newval,None)
            ret.next=temp
            ret=ret.next
            l1=l1.next
        while(l2!=None):
            newval=l2.val+c
            c=newval//10
            newval=newval%10
            temp=ListNode(newval,None)
            ret.next=temp
            ret=ret.next
            l2=l2.next
        if c>0:
            temp=ListNode(c,None)
            ret.next=temp
            ret=ret.next

        return retur.next
