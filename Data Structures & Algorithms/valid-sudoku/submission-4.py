class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols={}
        rows={}
        rowscols={}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in "0123456789":
                    continue
                if (i in cols.keys() and board[i][j] in cols[i]) or (j in rows.keys() and board[i][j] in rows[j]) or ((i//3,j//3) in rowscols.keys() and board[i][j] in rowscols[(i//3,j//3)]):
                    return False
                if i in cols.keys():
                    cols[i].append(board[i][j])
                else:
                    cols[i]=[board[i][j]]
                if j in rows.keys():
                    rows[j].append(board[i][j])
                else:
                    rows[j]=[board[i][j]]
                if (i//3,j//3) in rowscols.keys():
                    rowscols[(i//3,j//3)].append(board[i][j])
                else:
                    rowscols[(i//3,j//3)]=[board[i][j]]
        return True