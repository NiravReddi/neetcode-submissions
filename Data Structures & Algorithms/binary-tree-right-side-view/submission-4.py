# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=[root]
        if root==None:
            return []
        while q:
            res.append(q[-1].val)
            rt=[]
            for i in q:
                if i.left is not None:
                    rt.append(i.left)
                if i.right is not None:
                    rt.append(i.right)
            q=rt
        return res
            