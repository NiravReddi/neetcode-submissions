# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def makedic(root):
            dic={}
            if root==None:
                return 0
            dic[(root.val)]=root.val
            dic[(root.val,"left")]=makedic(root.left)
            dic[(root.val,"right")]=makedic(root.right)
            return dic
        sub=makedic(subRoot)
        def check(root):
            if root==None:
                return False
            if makedic(root)==sub:
                return True
            return check(root.left) or check(root.right)
        return check(root)
        
        