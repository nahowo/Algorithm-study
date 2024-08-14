import sys
input = sys.stdin.readline

def check(s):
    if s == 'l' or s == 'k' or s == 'p':
        return True
    return False

def solution():
    s1 = input().rstrip()[0]
    s2 = input().rstrip()[0]
    s3 = input().rstrip()[0]

    word = set()

    for i in [s1, s2, s3]:
        if check(i) == True:
            word.add(i)
    
    if len(word) == 3:
        return "GLOBAL"
    return "PONIX"

print(solution())