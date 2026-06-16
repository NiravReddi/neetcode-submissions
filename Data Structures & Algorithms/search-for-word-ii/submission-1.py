class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        res=[]
        f=0
        for k in words:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == k[0]:
                        if self.dfs(board, k, 0, i, j, m, n):
                            res.append(k)
                            f=1
                            break
                if f==1:
                    f=0
                    break
        
        return res
    
    def dfs(self, board: List[List[str]], word: str, index: int, i: int, j: int, m: int, n: int):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
            return False
        if index == len(word) - 1:
            return True
        
        board[i][j] = '#'
        
        if (self.dfs(board, word, index + 1, i - 1, j, m, n)
            or self.dfs(board, word, index + 1, i + 1, j, m, n)
            or self.dfs(board, word, index + 1, i, j - 1, m, n)
            or self.dfs(board, word, index + 1, i, j + 1, m, n)):
            board[i][j] = word[index]
            return True
        
        board[i][j] = word[index]
        return False