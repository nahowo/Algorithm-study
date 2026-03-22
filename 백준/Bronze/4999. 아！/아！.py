import sys
input = sys.stdin.readline

def solution():
    jaehwan = len(input().rstrip())
    doctor = len(input().rstrip())
    if jaehwan >= doctor:
        return "go"
    return "no"
    
print(solution())