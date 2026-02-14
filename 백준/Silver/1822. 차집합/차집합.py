import sys
input = sys.stdin.readline

def solution():
    answer = []
    na, nb = map(int, input().split())
    a = list(map(int, input().split()))
    b = set(map(int, input().split()))
    a.sort()

    for i in a:
        if i not in b:
            answer.append(i)
    return str(len(answer)) + "\n" + " ".join(map(str, answer))
    
print(solution())