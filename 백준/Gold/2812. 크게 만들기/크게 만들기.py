import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    number = input().rstrip()
    stack = []

    for i in range(n):
        while len(stack) > 0 and k > 0:
            if stack[-1] < number[i]:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(number[i])
    while k:
        stack.pop()
        k -= 1
    return ''.join(stack)
    
print(solution())