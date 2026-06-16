class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(i,j,d):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return 
            if grid[i][j]<d:
                return
            grid[i][j]=d
            dfs(i+1,j,d+1)
            dfs(i,j+1,d+1)
            dfs(i,j-1,d+1)
            dfs(i-1,j,d+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    dfs(i+1,j,1)
                    dfs(i,j+1,1)
                    dfs(i-1,j,1)
                    dfs(i,j-1,1)
        