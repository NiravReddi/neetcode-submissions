class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dic={}
        def  dfs(i,j):
            if i<0 or j<0 or j>=n or i>=m:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in dic.keys():
                return dic[i,j]
            dic[(i,j)]=dfs(i+1,j)+dfs(i,j+1)
            return dic[(i,j)]
        return dfs(0,0)
        