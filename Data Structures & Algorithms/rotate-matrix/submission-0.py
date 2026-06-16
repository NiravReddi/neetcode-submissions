class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(mat):
            for i in range(len(mat)):
                print(mat)
                for j in range(i,len(mat[0])):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
                
            
            return mat
        def reverse(mat):
            for i in range(len(mat)):
                mat[i]=mat[i][-1::-1]
            return mat
        matrix=transpose(matrix)
        matrix=reverse(matrix)
        
        