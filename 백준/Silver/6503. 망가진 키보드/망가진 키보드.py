import sys
input=sys.stdin.readline

def func(m):
    sentence=input().rstrip()
    d=dict()
    s=e=0
    cnt=0

    while e<len(sentence):
        if len(d)<m: # 아직 m 길이의 부분 문자열보다 짧을 때
            d[sentence[e]]=d.get(sentence[e],0)+1
            e+=1
        else:
            if sentence[e] in d: # 현재 s~h 사이에 이미 존재하는 단어인지 확인
                d[sentence[e]]+=1 # 있다면 뒤로 늘리기
                e+=1
            else:
                d[sentence[s]]-=1 # 없다면 앞에서 당기기
                if d[sentence[s]]==0:
                    del d[sentence[s]]
                s+=1
        if len(d)<=m:
            cnt=max(cnt,e-s)
    return cnt
            
while True:
    M=int(input())
    if M==0:
        break
    print(func(M))