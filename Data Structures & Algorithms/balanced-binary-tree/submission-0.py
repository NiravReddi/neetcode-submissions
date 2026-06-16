# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret=True
        def dfs(root):
            nonlocal ret
            if root==None:
                return 0
            else:
                left=1+dfs(root.left)
                right=1+dfs(root.right)
                if abs(left-right)<=1:
                    ret=(ret and True)
                else:
                    ret=(ret and False)
                return max(left,right)
        dfs(root)
        return ret
        