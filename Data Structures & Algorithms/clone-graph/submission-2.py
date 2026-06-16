"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        stack=[]
        visited={}
        if node==None:
            return None
        newnode=Node(node.val)
        
        newneigh=[]
        stack=[node]
        while(stack):
            currnode=stack.pop()
            r1=[]
            for i in currnode.neighbors:
                if i.val not in visited.keys():
                    neighbornode=Node(i.val)
                    visited[i.val]=neighbornode
                    stack.append(neighbornode)
                else:
                    r1.append(visited[i.val])
            currnode.neighbors=r1
        
        
        return newnode
        