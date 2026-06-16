# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret=[root.val]
        def dfs(root):
            if root==None:
                return 0
            else:
                leftval=dfs(root.left)
                rightval=dfs(root.right)
                leftval=max(leftval,0)
                rightval=max(rightval,0)
                ret[0]=max(ret[0],root.val+leftval+rightval)
                return root.val+max(leftval,rightval)
        dfs(root)
        return ret[0]
                