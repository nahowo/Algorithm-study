import sys
import heapq
input = sys.stdin.readline

def solution():
    n = int(input())
    pic = [] # [추천 횟수, 게시 시점, 학생 번호]
    r = int(input())
    rec = list(map(int, input().split()))
    picD = set()

    for i in range(r):
        if len(pic) < n: # 사진틀이 남아있는 경우
            if rec[i] in picD: # 이미 존재하는 학생인 경우
                for t in range(len(pic)):
                    if rec[i] == pic[t][2]:
                        pic[t][0] += 1
                        heapq.heapify(pic)
                        break
            else: # 존재하지 않는 학생인 경우
                picD.add(rec[i])
                heapq.heappush(pic, [1, i, rec[i]])

        else: # 사진틀이 남아있지 않는 경우
            if rec[i] in picD: # 이미 존재하는 학생인 경우
                for t in range(len(pic)):
                    if rec[i] == pic[t][2]:
                        pic[t][0] += 1
                        heapq.heapify(pic)
                        break
            else: # 존재하지 않는 학생인 경우
                removed = heapq.heappop(pic)
                picD.remove(removed[2])
                picD.add(rec[i])
                heapq.heappush(pic, [1, i, rec[i]])
            
    result = []
    for i in range(len(pic)):
        result.append(pic[i][2])
    result.sort()
    return result

print(*solution())