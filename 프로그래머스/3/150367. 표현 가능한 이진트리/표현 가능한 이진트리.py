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

def recursion(n, start, end):
    if start >= end:
        return 1

    mid = (start + end) // 2

    if n[mid] == '0' and n[start : end].count('1') > 0:
        return 0
    return recursion(n, start, mid - 1) & recursion(n, mid + 1, end)

def solution(numbers):
    def check(i, s):
        if answer[i] and (L:=(len(s)//2)):
            if s[L]=='0' and ('1' in s):
                answer[i] = 0
            else:
                check(i, s[:L]), check(i, s[L+1:])
    
    answer = [1] * len(numbers)

    for i in range(len(numbers)):
        tmpN = binary(numbers[i])
        # tmpL = len(tmpN)
        check(i, tmpN)

    return answer