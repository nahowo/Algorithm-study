import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    bit = str(bin(n))[2:][::-1]
    answer = 0
    sqr = 1
    for i in range(len(bit)):
        if bit[i] == '1':
            answer += sqr
        sqr *= 3
    return answer

print(solution())