import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip()
    cnt = {i: 0 for i in range(97, 123)}
    for i in s:
        if 97 <= ord(i.lower()) <= 122:
            cnt[ord(i.lower())] += 1
    
    answer = min(cnt.values())
    if answer >= 3:
        return "Triple pangram!!!"
    elif answer == 2:
        return "Double pangram!!"
    elif answer == 1:
        return "Pangram!"
    return "Not a pangram"
    
n = int(input())
for i in range(n):
    print("Case " + str(i + 1) + ": " + solution())