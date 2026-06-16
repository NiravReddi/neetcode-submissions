class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(i,s):
            nonlocal res,k
            if len(s)==k:
                res.append(sorted(s))
                return
            if i==n+1:
                return 
            else:
                for p in range(i,n+1):
                    s.append(p)
                    dfs(p+1,s)
                    s.pop()
        dfs(1,list())
        return res
        