# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(start,size):
            prev=None
            first=start
            while(start!=None and size>0):
                temp=start.next
                start.next=prev
                prev=start
                start=temp
                size-=1
            return first,prev,temp
        ret=ListNode(0,head)
        curr=ret.next
        prev=ret
        i=1
        while(i<left):
            prev=curr
            curr=curr.next
            i+=1
        end,start,endnext=reverse(curr,right-left+1)
        prev.next=start
        end.next=endnext
        return ret.next
            
        