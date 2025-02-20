def solution(n, w, num):
    answer = 0
    # 층이 짝수면 왼쪽 -> 오른쪽
    # 층이 홀수면 오른쪽 -> 왼쪽
    h1 = ((num - 1) // w)
    h2 = ((n - 1) // w)
    
    p1 = ((num - 1) % w)
    if h1 % 2 == 1:
        p1 = w - p1 - 1
    
    top = [0] * w
    p2 = ((n - 1) % w)
    if h2 % 2 == 1:
        p2 = w - p2 - 1
        for i in range(p2, w):
            top[i] = 1
    else:
        for i in range(p2 + 1):
            top[i] = 1
    answer = h2 - h1 + top[p1]
    return answer