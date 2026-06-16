# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret=ListNode()
        retu=ret
        ind=0
        while(len(lists)>0):
            mn=lists[0]
            ind=0
            mnind=0
            for i in lists:
                if mn.val>i.val:
                    mn=i
                    mnind=ind
                ind+=1
            ret.next=mn
            lists[mnind]=lists[mnind].next
            if lists[mnind]==None:
                lists.pop(mnind)
            ret=ret.next
        return retu.next            
            