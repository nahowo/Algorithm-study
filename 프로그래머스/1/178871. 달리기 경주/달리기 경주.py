def solution(players, callings):
    order = dict()
    for i, name in enumerate(players):
        order[name] = i
    
    for c in callings:
        co = order[c]
        overtaker = players[co]
        overtaken = players[co - 1]
        order[overtaken] += 1
        order[overtaker] -= 1
        players[co], players[co - 1] = overtaken, overtaker
    return players