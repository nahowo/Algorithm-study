import sys
input = sys.stdin.readline

def solution():
    m = int(input())
    series = dict()
    for _ in range(m):
        d, s, e = map(int, input().split())
        if d in series:
            series[d].append([e, s])
        else:
            series[d] = [[e, s]]
        
    for k, v in series.items():
        series[k] = sorted(v)
    
    cnt = 0
    for day, arr in series.items():
        timeTable = [0] * 2400

        for end, start in arr:
            flag = False
            for i in range(start, end):
                if timeTable[i] == 1:
                    flag = True
                    break
            if not flag:
                for i in range(start, end):
                    timeTable[i] = 1
                cnt += 1

    return cnt
    
n = int(input())
answers = []
for _ in range(n):
    answers.append(solution())

for i in range(n):
    print("Scenario #" + str(i + 1) + ":")
    print(answers[i])
    if i < n - 1:
        print()