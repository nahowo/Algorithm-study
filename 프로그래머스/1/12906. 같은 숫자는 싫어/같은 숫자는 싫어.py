def solution(arr):
    answer = [-1]
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    return answer[1:]