# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret=ListNode(0,None)
        head=ret
        while(len(lists)>0):
            assign=None
            ind=0
            recind=1002
            for i in lists:
                if assign==None and i!=None:
                    assign=i
                    recind=ind
                elif assign.val > i.val:
                    assign=i
                    recind=ind
                ind+=1
            head.next=assign
            head=head.next
            if lists[recind].next != None:
                lists[recind]=lists[recind].next
            else:
                lists.pop(recind)
        return ret.next
        
            
