# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if root==None:
                return []
            else:
                l1=dfs(root.left)
                d=[root.val]
                l2=dfs(root.right)
                r1=l1
                r1.extend(d)
                r1.extend(l2)
                return r1
        
        return dfs(root)[k-1]

        