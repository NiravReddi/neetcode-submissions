# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root==None:
            return []
        q=[root]
        while(q):
            r1=[]
            ret=[]
            for i in q:
                ret.append(i.val)
                if i.left!=None:
                    r1.append(i.left)
                if i.right!=None:
                    r1.append(i.right)
            res.append(ret)
            q=r1
        return res