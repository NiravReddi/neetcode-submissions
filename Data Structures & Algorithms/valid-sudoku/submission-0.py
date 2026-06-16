class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic_x=defaultdict(list)
        dic_y=defaultdict(list)
        squares = defaultdict(list)  
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    continue
                if board[i][j] in  dic_x[i] or board[i][j]in dic_y[j] or board[i][j] in squares[(i//3,j//3)]:
                    return False
                dic_x[i].append(board[i][j])
                dic_y[j].append(board[i][j])
                squares[(i//3,j//3)].append(board[i][j])
        return True
