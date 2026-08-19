# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def makedic(root):
            dic={}
            if root==None:
                return 0
            dic[(root.val)]=root.val
            dic[(root.val,"left")]=makedic(root.left)
            dic[(root.val,"right")]=makedic(root.right)
            return dic
        return makedic(p)==makedic(q)
