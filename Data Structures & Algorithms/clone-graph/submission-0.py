"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        dic={}
        def pop(root):
            if root in dic:
                return dic[root]
            copy=Node(root.val)
            dic[root]=copy
            for i in root.neighbors:
                copy.neighbors.append(pop(i))
            return copy
        return pop(node) if node else None


        