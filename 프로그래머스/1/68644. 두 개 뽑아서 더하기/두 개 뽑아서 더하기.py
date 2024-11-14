def solution(numbers):
    answer = []
    check = [False] * 201
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                check[numbers[i] + numbers[j]] = True
    for i in range(0, 201):
        if check[i]:
            answer.append(i)
            
    return answer