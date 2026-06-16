# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        ret=ListNode(0,None)
        res=ret
        while(l1!=None and l2!=None):
            add=l1.val+l2.val+c
            if add<10:
                c=0
                addn=ListNode(add)
            else:
                if add>=20:
                    c=2
                else:
                    c=1
                addn=ListNode(add%10)
            res.next=addn
            res=res.next
            l1=l1.next
            l2=l2.next
        while(l1!=None ):
            add=l1.val+c
            if add<10:
                c=0
                addn=ListNode(add)
            else:
                if add>=20:
                    c=2
                else:
                    c=1
                addn=ListNode(add%10)
            res.next=addn
            res=res.next
            l1=l1.next
        while(l2!=None ):
            add=l2.val+c
            if add<10:
                c=0
                addn=ListNode(add)
            else:
                if add>=20:
                    c=2
                else:
                    c=1
                addn=ListNode(add%10)
            res.next=addn
            res=res.next
            l2=l2.next
        if c!=0:
            add=ListNode(c)
            res.next=add
            res=res.next
        return ret.next
            
        
        