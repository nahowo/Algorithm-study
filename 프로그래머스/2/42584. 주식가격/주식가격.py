def solution(prices):
    n = len(prices)
    answer = [i for i in range(n - 1, -1, -1)]
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
    return answer