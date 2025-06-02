import sys, math
input = sys.stdin.readline
click = lambda x: 0 if x else 1

def click(i):
    if switch[i]:
        switch[i] = 0
    else:
        switch[i] = 1

def solution():
    global switch, n
    n = int(input())
    switch = list(map(int, input().split()))
    m = int(input())
    
    for _ in range(m):
        gender, button = map(int, input().split())
        if gender == 1:
            boyClick(button)
        else:
            girlClick(button)

    answer = []
    for i in range(0, len(switch), 20):
        answer.append(' '.join(map(str, switch[i : i + 20])))
    return '\n'.join(answer)

def boyClick(button):
    for i in range(button, n + 1, button):
        click(i - 1)

def girlClick(button):
    s = button - 2
    e = button
    click(button - 1)
    while s >= 0 and e < n:
        if switch[s] == switch[e]:
            click(s)
            click(e)
            s -= 1
            e += 1
        else:
            break

print(solution())