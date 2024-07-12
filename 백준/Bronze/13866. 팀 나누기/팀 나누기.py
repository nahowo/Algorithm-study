import sys
input = sys.stdin.readline

def solution():
    team = list(map(int,input().split()))
    team.sort()

    return abs(team[0] + team[3] - team[1] - team[2])

print(solution())