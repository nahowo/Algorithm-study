def popStack(stack): # 스택 제거하기
    popCount=0
    while len(stack)>=2:
        if stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
            popCount+=2
        else:
            break
    return popCount

def solution(board, moves): # 스택 추가하기
    answer=0
    stack=[]
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1]!=0:
                stack.append(board[i][j-1])
                board[i][j-1]=0
                answer+=popStack(stack)
                break
    return answer