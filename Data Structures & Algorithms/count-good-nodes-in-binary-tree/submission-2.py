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
            if root==None:
                return
            nonlocal res
            if root.val>=mx:
                res+=1
            dfs(root.left,max(mx,root.val))
            dfs(root.right,max(mx,root.val))
        dfs(root,-1001)
        return res