import sys
import heapq
input=sys.stdin.readline

def func():
    n=int(input())
    pos=[] # 양수 리스트
    neg=[] # 음수 리스트
    for _ in range(n):
        tmp=int(input())
        if tmp>0:
            heapq.heappush(pos,tmp)
        elif tmp<0:
            heapq.heappush(neg,(-1)*tmp)
        else:
            if len(pos)==0 and len(neg)==0: # 두 리스트 모두 빈 경우
                print(0)
            elif len(pos)==0 and len(neg)>0: # 양수 리스트만 존재할 경우
                print(heapq.heappop(neg)*(-1))
            elif len(neg)==0 and len(pos)>0: # 음수 리스트만 존재할 경우
                print(heapq.heappop(pos))
            else: # 두 배열 다 존재할 경우
                tmpp=pos[0]
                tmpn=neg[0]
                if tmpp<tmpn:
                    print(heapq.heappop(pos))
                else: # 절댓값이 여러개(음수, 양수 절댓값이 같을 때)일 경우 음수를 출력
                    print(heapq.heappop(neg)*(-1))

func()