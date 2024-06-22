'''
준 사람*받은 사람 형식의 2차원 배열 생성
{사람: [준 선물 수, 받은 선물 수], ... } 형식의 딕셔너리 생성
다음 달 받을 선물 수, ... 형식의 배열 생성

gifts 순회
    2차원 배열, 딕셔너리 채워넣기

사람 1 순회
    사람 2 순회
        if 사람 1과 사람 2가 다를 때:
            사람 1과 사람 2가 주고받은 선물 비교
            if 동일:
                사람 1과 사람 2의 선물 지수 비교
                받는 사람의 다음달 받을 선물 수 증가

필요 함수: 입력 출력 담당, 주고받은 선물 비교 담당, 선물 지수 비교 담당
'''
def exchangedPresent(presentArr, a, b, person): # 주고받은 선물 비교 함수
    if presentArr[person[a]][person[b]] > presentArr[person[b]][person[a]]:
        return a
    elif presentArr[person[a]][person[b]] < presentArr[person[b]][person[a]]:
        return b
    else:
        return False
    
def presentPoint(presentDict, a, b): # 선물 지수 비교 함수
    aPoint = presentDict[a][0] - presentDict[a][1]
    bPoint = presentDict[b][0] - presentDict[b][1]
    if aPoint > bPoint:
        return a
    elif aPoint < bPoint:
        return b
    else:
        return False
    
def solution(friends, gifts):
    answer = 0
    presentArr = [[0]*(len(friends)) for _ in range(len(friends))]
    presentDict = dict()
    nextPresent = [0]*(len(friends))
    person = dict()
    for i in range(len(friends)):
        presentDict[friends[i]] = [0, 0] # [준 선물 수, 받은 선물 수]
        person[friends[i]]=i # 사람에게 인덱스 부여
    
    for i in range(len(gifts)):
        giver, receiver = gifts[i].split()
        presentArr[person[giver]][person[receiver]] += 1
        presentDict[giver][0] += 1
        presentDict[receiver][1] += 1
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                tmp1 = exchangedPresent(presentArr, friends[i], friends[j], person)
                if tmp1 != False:
                    print(tmp1)
                    nextPresent[person[tmp1]] += 1
                else:
                    tmp2 = presentPoint(presentDict, friends[i], friends[j])
                    if tmp2 != False:
                        print(tmp2)
                        nextPresent[person[tmp2]] += 1
    print(presentArr)
    print(presentDict)
    print(person)
    print(nextPresent)
    answer = max(nextPresent) // 2 # 두 번씩 비교하므로 2로 나누기
    
    return answer