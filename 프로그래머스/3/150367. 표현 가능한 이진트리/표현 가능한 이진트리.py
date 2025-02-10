def binary(n):
    result = ""
    cnt = 1
    while n >= 1:
        result += str(n % 2)
        n //= 2
    if n == 1:
        result += str(n)
    while (2 ** cnt - 1) < len(result):
        cnt += 1
    result += '0' * ((2 ** cnt - 1) - len(result))
    
    return result[::-1]

def recursion(n):
    if len(n) <= 1:
        return 1
    mid = len(n) // 2

    if n[mid] == '0' and '1' in n:
        return 0
    return recursion(n[: mid]) & recursion(n[mid + 1 :])

def solution(numbers):    
    answer = [0] * len(numbers)

    for i in range(len(numbers)):
        tmpN = binary(numbers[i])
        answer[i] = recursion(tmpN)

    return answer