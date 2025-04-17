def toN(n, number):
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    ret = ''
    while number:
        ret += arr[number % n]
        number //= n
    
    return ret[::-1]

def solution(n, t, m, p):
    answer = ''
    length = 0
    number = 0
    total = ' 0'

    while length < (t * m):
        s = toN(n, number)
        total += s
        length += len(s)
        number += 1

    pos = p
    for i in range(t):
        answer += total[pos]
        pos += m
        
    return answer