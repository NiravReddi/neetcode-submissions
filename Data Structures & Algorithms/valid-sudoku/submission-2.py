class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        cols={}
        rowscols={}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]=='.':
                    continue
                if (i in rows.keys() and board[i][j] in rows[i]) or ( j in cols.keys() and board[i][j] in cols[j]) or ((i//3,j//3) in rowscols.keys() and board[i][j] in rowscols[(i//3,j//3)]):
                    return False
                if i in rows.keys():
                    rows[i].append(board[i][j])
                else:
                    rows[i]=[board[i][j]]
                if j in cols.keys():
                    cols[j].append(board[i][j])
                else:
                    cols[j]=[board[i][j]]
                if (i//3,j//3) in rowscols.keys():
                    rowscols[(i//3,j//3)].append(board[i][j])
                else:
                    rowscols[(i//3,j//3)]=[board[i][j]]   
        return True             

        