def rotate(x1, y1, x2, y2):
    global board
    tmp = board[x1 + 1][y1]
    for x in range(x1 + 1, x2):
        board[x][y1] = board[x + 1][y1]
    for y in range(y1, y2):
        board[x2][y] = board[x2][y + 1]
    for x in range(x2, x1, -1):
        board[x][y2] = board[x - 1][y2]
    for y in range(y2, y1, -1):
        board[x1][y] = board[x1][y - 1]
    board[x1][y1] = tmp

    ret = 10 ** 4
    for x in range(x1, x2 + 1):
        ret = min([ret, board[x][y1], board[x][y2]])
    for y in range(y1, y2 + 1):
        ret = min([ret, board[x1][y], board[x2][y]])
    
    return ret

def solution(rows, columns, queries):
    global board
    answer = [0] * len(queries)
    board = [[0] * (columns) for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = (i * (columns) + j) + 1
    
    for i, v in enumerate(queries):
        x1, y1, x2, y2 = v[0] - 1, v[1] - 1, v[2] - 1, v[3] - 1
        answer[i] = rotate(x1, y1, x2, y2)
        
    return answer