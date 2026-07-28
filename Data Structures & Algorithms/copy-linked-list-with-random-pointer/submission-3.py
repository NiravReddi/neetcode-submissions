"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={None:None}
        head1=head
        while(head1!=None):
            newnode=Node(head1.val)
            dic[head1]=newnode
            head1=head1.next
        head1=head
        while(head1!=None):
            copy=dic[head1]
            copy.next=dic[head1.next]
            copy.random=dic[head1.random]
            head1=head1.next
        return dic[head]

            