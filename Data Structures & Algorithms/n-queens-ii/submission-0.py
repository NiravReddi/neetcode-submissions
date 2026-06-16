class Solution:
    def totalNQueens(self, n: int) -> int:
        
        ret=[]
        res=[['.' for i in range(n)] for j in range(n)]

        def check(i,j,board):
            rowcheck=False
            colcheck=False
            diagonalcheck=False

            for k in range(len(board)):
                if board[k][j]=='Q':
                    colcheck=True
                    break
                if board[i][k]=='Q':
                    rowcheck=True
                    break
            k,p=i,j
            while(k>=0 and p>=0):
                if board[k][p]=='Q':
                    diagonalcheck=True
                    break
                k-=1
                p-=1
            k,p=i,j
            while(k<len(board) and p<len(board[0])):
                if board[k][p]=='Q':
                    diagonalcheck=True
                    break
                k+=1
                p+=1
            k,p=i,j
            while(k>=0 and p<len(board[0])):
                if board[k][p]=='Q':
                    diagonalcheck=True
                    break
                k-=1
                p+=1
            k,p=i,j
            while(p>=0 and k<len(board)):
                if board[k][p]=='Q':
                    diagonalcheck=True
                    break
                k+=1
                p-=1
            if colcheck or rowcheck or diagonalcheck:
                return False
            return True
        def add(board):
            nonlocal ret
            bd=[]
            row=""
            for i in range(n):
                row="".join(board[i])
                bd.append(row)
            ret.append(bd)
        def dfs(i,board):
            if i==n-1:
                for j in range(n):
                    if check(i,j,board):
                        
                        board[i][j]='Q'
                        add(board)
                        board[i][j]='.'
            else:
                for j in range(n):
                    if check(i,j,board):
                        board[i][j]='Q'
                        dfs(i+1,board.copy())
                        board[i][j]='.'
        dfs(0,res.copy())
        return len(ret)

                
            