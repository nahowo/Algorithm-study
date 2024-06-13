# 문자열 순회
#     점수, 보너스: 점수 스택에 추가
#     if 옵션: 
#         스타상: 스택 pop, *2 적용 후 스택에 추가, 점수*2 스택에 추가
#         아차상: 점수*-1 스택에 추가
# 스택 총합 반환

def solution(dartResult):
    bonusDict={'S':1,'D':2,'T':3}
    answer=0
    i=0
    stack=[]
    
    while i<len(dartResult):
        if dartResult[i]=='*':
            score=stack.pop()
            if len(stack)>0:
                prevScore=stack.pop()
                stack.append(prevScore*2)
            stack.append(score*2)
            i+=1
            
        elif dartResult[i]=='#':
            score=stack.pop()
            stack.append(score*-1)
            i+=1
            
        else:
            if dartResult[i:i+2]=='10': # 점수가 10인 경우 예외처리
                score=10
                bonus=dartResult[i+2]
                i+=1
            else:
                score=dartResult[i]
                bonus=dartResult[i+1]
            stack.append(int(score)**bonusDict[bonus])
            i+=2
            
    answer=sum(stack)
    return answer

# 시간복잡도: O(len(dartResult))