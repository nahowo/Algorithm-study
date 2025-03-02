def solution(number, k):
    answer = []
    for i in range(len(number)):
        while k:
            if len(answer) > 0 and number[i] > answer[-1]:
                answer.pop()
                k -= 1
            else:
                break
        answer.append(number[i])
    while k:
        answer.pop()
        k -= 1
    
    return ''.join(answer)