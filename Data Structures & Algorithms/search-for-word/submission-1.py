class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        exists = False
        
        def dfs(r, c, index):
            if index == len(word):
                return True

            if (r not in range(ROWS) or c not in range(COLS) 
            or word[index] != board[r][c]) or (r, c) in path:
                return False

            path.add((r, c))

            res = (dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or 
            dfs(r, c - 1, index + 1) or dfs(r, c + 1, index + 1))
            path.remove((r, c))
            return res
    
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    exists = exists or dfs(i, j, 0)
        
        return exists