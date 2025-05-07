class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]
        m = len(board)
        n = len(board[0])
        neighbors = [[[0, 0] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        neighbors[i][j][board[ni][nj]] += 1
                
        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    if 2 > neighbors[i][j][1] or neighbors[i][j][1] > 3:
                        board[i][j] = 0
                else:
                    if neighbors[i][j][1] == 3:
                        board[i][j] = 1