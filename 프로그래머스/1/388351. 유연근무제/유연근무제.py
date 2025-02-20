def calcTime(t):
    t += 10
    if t % 100 >= 60:
        t += 100
        t -= 60
    return t

def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    maxTime = [0] * n
    for i in range(n):
        maxTime[i] = calcTime(schedules[i])
    
    for p in range(n):
        flag = True
        for day in range(startday, startday + 7):
            d = ((day - 1) % 7) + 1
            if d >= 6:
                continue
            if timelogs[p][d - startday] > maxTime[p]:
                flag = False
                break
        if flag:
            answer += 1
    return answer