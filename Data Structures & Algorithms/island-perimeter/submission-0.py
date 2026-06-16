class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir=[1,-1]
        res=0
        visited=set()
        def dfs(i,j):
            nonlocal visited,res,dir
            if (i,j) in visited:
                return True
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
                return False
            res+=4
            visited.add((i,j))
            for k in dir:
                if dfs(i+k,j) is True:
                    res-=1
                if dfs(i,j+k) is True:
                    res-=1
            return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]==1:
                    dfs(i,j)
        return res