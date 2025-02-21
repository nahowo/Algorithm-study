def solution(prices):
    n = len(prices)
    answer = [i for i in range(n - 1, -1, -1)]
    stack = [] # [index, price]
    for i in range(n):
        while stack: # 현재 인덱스보다 이전 인덱스만 스택에 존재
            if stack[-1][1] > prices[i]: # stack[-1] 인덱스 가격이 현재가격보다 큼 -> 가격 하락
                xIdx, xVal = stack.pop()
                answer[xIdx] = i - xIdx
            else:
                break
        stack.append([i, prices[i]])
    return answer