class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(list)
        cols=defaultdict(list)
        rowscols=defaultdict(list)
        for i in range(len(board)):
            for j  in range(len(board[0])):
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in rowscols[tuple(str(i//3)+str(j//3))]:
                    return False
                if board[i][j]!='.':
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])
                    rowscols[tuple(str(i//3)+str(j//3))].append(board[i][j])
        return True

        