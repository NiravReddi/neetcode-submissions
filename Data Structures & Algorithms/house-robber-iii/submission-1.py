# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res=0
        dic={}
        def dfs(root,flag):
            nonlocal dic
            if (root,flag) in dic.keys():
                return dic[(root,flag)]
            if root==None:
                return 0
            if flag:
                
                left=dfs(root.left,not flag)
                right=dfs(root.right,not flag)
                
                dic[(root,flag)]=left+right+root.val
                return left+right+root.val
            else:
                left=dfs(root.left,not flag)
                right=dfs(root.right,not flag)
                left1=dfs(root.left,flag)
                right1=dfs(root.right,flag)
                left=max(left,left1)
                right=max(right,right1)
                dic[(root,flag)]=left+right
                return left+right
        r1=dfs(root,True)
        dic={}
        r2=dfs(root,False)
        print(r1,r2)
        res=max(res,r1,r2)
        return res