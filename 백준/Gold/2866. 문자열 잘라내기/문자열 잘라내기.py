import sys
input=sys.stdin.readline

def func():
    r,c=map(int,input().split()) # 문자열을 열 기준으로 저장
    tmp_arr=['']*c
    for i in range(r):
        word=input()
        for j in range(c):
            tmp_arr[j]+=word[j]

    set1=set(tmp_arr)
    count=0
    for _ in range(r-1):
        set2=set()
        for j in set1: # 각 문자열의 앞 문자 슬라이싱
            keyword=j[1:]
            if keyword not in set2: # 중복 체크
                set2.add(keyword)
            else:
                return count # 중복이 존재한다면 바로 종료
        count+=1 # 행에 중복이 없다면 count값 증가
        set1=set2
    return count
print(func())