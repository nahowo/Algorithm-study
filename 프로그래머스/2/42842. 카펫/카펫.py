def solution(brown, yellow):
    cntBrown = lambda x, y: (2 * x + 2 * (y - 2))
    cntYellow = lambda x, y: ((x - 2) * (y - 2))
    answer = [0,0]
    
    for i in range(3, brown - 2): # 가로
        for j in range(3, brown - 2): # 세로
            if cntBrown(i, j) == brown and cntYellow(i, j) == yellow:
                answer = [i, j]
    answer.sort(reverse = True)
    return answer