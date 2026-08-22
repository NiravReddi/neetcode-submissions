# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            nenode=TreeNode(val)
            return nenode
        if val<=root.val:
            if root.left==None:
                nenode=TreeNode(val)
                root.left=nenode
            else:
                self.insertIntoBST(root.left,val)
        else:
            if root.right==None:
                nenode=TreeNode(val)
                root.right=nenode
            else:
                self.insertIntoBST(root.right,val)
        return root
        