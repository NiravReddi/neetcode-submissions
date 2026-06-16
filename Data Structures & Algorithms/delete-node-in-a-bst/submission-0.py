# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def return_leftmost(root):
            if root.left==None:
                return root
            return return_leftmost(root.left)
        def delete(root):
            if root.right!=None:
                ret=root.right
                leftmost=return_leftmost(root.right)
                leftmost.left=root.left
                return ret
            else:
                ret=root.left
                return root.left
        if root and root.val==key:
            return delete(root)
        elif root and root.val > key:
            root.left=self.deleteNode(root.left,key)
        elif root:
            root.right=self.deleteNode(root.right,key)
        return root