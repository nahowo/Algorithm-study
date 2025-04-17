def solution(dirs):
    direction = {'U': [1, 0], 'D': [-1, 0], 'R': [0, 1], 'L': [0, -1]}
    x, y = 0, 0
    visited = set()
    
    for d in dirs:
        dx, dy = direction[d]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny
    
    answer = len(visited) // 2
    return answer