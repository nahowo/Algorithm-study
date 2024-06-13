# 배열 순회
#     지도 1 | 지도 2 연산 -> 전체 지도 계산
#     전체 지도 비트를 문자열로 변환

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bit=bin(arr1[i]|arr2[i])
        answer.append(toString(bit,n))
    return answer

# 이진수를 지도 문자열로 바꾸는 함수
def toString(bit,n):
    mapStr=[' ']*n
    bit='0'*(n-(len(bit)-2))+bit[2:]
    for i in range(n):
        if bit[i]=='1':
            mapStr[i]='#'
    return ''.join(mapStr)
    