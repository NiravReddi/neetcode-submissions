# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(root,l):
            nonlocal res
            if root==None:
                return
            else:
                t=True
                for i in l:
                    if i>root.val:
                        t=(t and False)
                if t:
                    res+=1
                dfs(root.left,l+[root.val])
                dfs(root.right,l+[root.val])
        dfs(root,[])
        return res
        