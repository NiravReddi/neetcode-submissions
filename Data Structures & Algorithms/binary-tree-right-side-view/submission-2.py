# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root==None:
            return res
        queue=[root]
        while(len(queue)!=0):
            print(queue[len(queue)-1].val)
            res.append(queue[len(queue)-1].val)
            r1=[]
            for i in queue:
                if i.left!=None:
                    r1.append(i.left)
                if i.right!=None:
                    r1.append(i.right)
            queue=r1
        return res
        