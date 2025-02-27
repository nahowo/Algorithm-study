import sys
input = sys.stdin.readline

def solution():
    n = input().rstrip()
    number = {str(i): 0 for i in range(10)}
    cnt = 0

    for i in n:
        if number[i] < 1:
            if i == '6' and number['9'] > 0:
                number['9'] -= 1
            elif i == '9' and number['6'] > 0:
                number['6'] -= 1
            else:
                cnt += 1
                for j in range(10):
                    number[str(j)] += 1
                number[i] -= 1
        else:
            number[i] -= 1
    return cnt

print(solution())