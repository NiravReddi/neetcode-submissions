# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        queue=[root]
        ret=[]
        while(len(queue)!=0):
            r=[]
            r1=[]
            for i in queue:
                r1.append(i.val)
                if i.left!=None:
                    r.append(i.left)
                if i.right!=None:
                    r.append(i.right)
            queue=r
            ret.append(r1)
        return ret