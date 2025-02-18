def dfs(route, cnt, tickets):
    global answer
    if cnt == n + 1:
        if len(answer) == 0:
            answer = route.copy()
        else:
            answer = min(answer, route.copy())
        return
    
    for i in range(n):
        if tickets[i][2] and tickets[i][0] == route[-1]:
            tickets[i][2] = 0
            dfs(route + [tickets[i][1]], cnt + 1, tickets)
            tickets[i][2] = 1

def solution(tickets):
    global n, answer
    answer = []
    n = len(tickets)
    tickets.sort(key = lambda x: x[1])
    for i in range(n):
        tickets[i].append(1)
    route = ["ICN"]
    dfs(route, 1, tickets)
    
    return answer