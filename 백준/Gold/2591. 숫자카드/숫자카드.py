import sys
input = sys.stdin.readline

def rec(idx):
    if idx > len(number):
        return 0
    if idx == len(number):
        return 1
    if cache[idx] != -1:
        return cache[idx]
    
    if idx == len(number) - 1:
        if int(number[idx]) != 0: # 맨 뒤 카드가 0일 수 없음
            return 1
        else:
            return 0
    
    ret = 0
    if number[idx] != '0':
        # 한자리
        ret += rec(idx + 1)
        # 두자리
        if int(number[idx : idx + 2]) <= 34:
            ret += rec(idx + 2)

    cache[idx] = ret
    return ret
    
def solution():
    global number, cache
    number = input().rstrip()
    cache = [-1] * len(number)
    return rec(0)

print(solution())