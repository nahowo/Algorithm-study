def solution(n):
    DIV = 1234567
    answer = 0
    fibo = [0] * (n + 1)
    fibo[1] = 1
    for i in range(2, n + 1):
        fibo[i] = (fibo[i - 1]) % DIV + (fibo[i - 2]) % DIV
        fibo[i] %= DIV
    answer = fibo[n]
    return answer