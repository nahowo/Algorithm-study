import sys
input = sys.stdin.readline

def formating(s, n):
    return '0' * (n - len(s)) + s

def solution():
    sh, sm = input().rstrip().split()
    eh, em = input().rstrip().split()

    sh = formating(sh, 2)
    sm = formating(sm, 2)
    eh = formating(eh, 2)
    em = formating(em, 2)

    s = sh + sm
    e = eh + em
    n = input().rstrip()
    cnt = 0

    while True:
        if int(s) == int(e) + 1:
            break
        if int(s[2:]) == 60:
            s = formating(str(int(s) + 40), 4)
        
        if n in s:
            cnt += 1
        s = formating(str(int(s) + 1), 4)

    return cnt

print(solution())