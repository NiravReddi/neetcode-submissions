# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[[root]]
        res=[]
        if root==None:
            return []
        while(len(q)>0):
            ress=[]
            ret=[]
            curr=q.pop(0)
            for i in curr:
                if i.left!=None:
                    ret.append(i.left)
                if i.right!=None:
                    ret.append(i.right)
                ress.append(i.val)
            if ret!=[]:
                q.append(ret)
            res.append(ress)
        return res
                
        