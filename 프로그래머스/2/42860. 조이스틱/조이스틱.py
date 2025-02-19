def solution(name):
    n = len(name)
    cnt = [0] * n
    for i in range(n):
        cnt[i] = min(ord(name[i]) - 65, 91 - ord(name[i]))

    answer = 0
    rem = 0
    move = 20
    
    for i in range(n):
        if cnt[i] > 0:
            answer += cnt[i]
            if i == 0:
                continue
            tmp = rem + n - i
            move = min(move, min(tmp + rem, tmp + n - i))
            rem = i
    answer += min(rem, move)
    return answer