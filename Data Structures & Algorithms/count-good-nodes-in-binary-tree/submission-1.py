# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(root,mx):
            nonlocal res
            if root is None:
                return 
            if mx<=root.val:
                res+=1
            mx=max(mx,root.val)
            dfs(root.left,mx)
            dfs(root.right,mx)
        dfs(root,-101)
        return res
        