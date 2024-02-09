import sys
input=sys.stdin.readline

def func():
    stamina=int(input())%100

    zone=0
    for i in range(1,5): # 콘의 개수만큼 반복
        for k in range(2): # 왕복 2번
            for j in range(i): # 콘마다 왕복
                if stamina>=5: # 다음 콘으로 이동 가능한 경우
                    if k==0:
                        zone+=1
                    else:
                        zone-=1
                    stamina-=5

                if stamina<5: # 다음 칸으로 이동할 수 없는 경우
                    if stamina==0: # 아예 이동할 수 없는 경우
                        return zone
                    else:
                        if zone==0: # 시작점에서 다시 돌아가야 하는 경우
                            return zone+1
                        elif zone==i: # 맨 끝 콘에서 다시 돌아가야 하는 경우
                            return zone
                        else: # 중간 콘일 경우
                            if k==0: # 더 앞으로 가야 하는 경우
                                return zone+1
                            else: # 더 뒤로 가야 하는 경우
                                return zone

print(func())