# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            def inord(root):
                if root==None:
                    return "+"
                return inord(root.right)+str(root.val)+inord(root.left)
            def postord(root):
                if root==None:
                    return "+"
                return postord(root.right)+postord(root.left)+str(root.val)
            if inord(p)==inord(q) and postord(p)==postord(q):
                return True
            return False
        ls=[root]
        while(len(ls)!=0):
            curr=ls.pop(0)
            if curr.left!=None:
                ls.append(curr.left)
            if curr.right!=None:
                ls.append(curr.right)
            if curr.val==subRoot.val:
                if isSame(curr,subRoot):
                    return True
        return False