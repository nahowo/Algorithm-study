def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    dp1 = [0] * (n + 2)
    dp1[1] = sticker[0]
    
    for i in range(2, n): # 첫 스티커 선택
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i - 1])
    dp1[n] = dp1[n - 1]
    
    dp2 = [0] * (n + 2)
    dp2[2] = sticker[1]
    
    for i in range(2, n + 1): # 첫 스티커 선택 X
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i - 1])

    answer = max(dp1[n], dp2[n])
    return answer