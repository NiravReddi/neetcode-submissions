class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def dfs(i,j):
            for k in range(len(matrix[i])):
                matrix[i][k]=0
            for k in range(len(matrix)):
                matrix[k][j]=0 
        s=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    s.add((i,j))
        for k in s:
            dfs(k[0],k[1])