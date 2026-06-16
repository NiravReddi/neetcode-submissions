# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inord(root):
            if root==None:
                return "-"
            return inord(root.right)+str(root.val)+inord(root.left)
        def postord(root):
            if root==None:
                return "+"
            return postord(root.right)+postord(root.left)+str(root.val)
        
        if postord(p)==postord(q) and inord(p)==inord(q):
            return True
        else:
            return False