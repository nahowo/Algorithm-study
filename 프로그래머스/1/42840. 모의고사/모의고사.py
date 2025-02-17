def solution(answers):
    correct = [0, 0, 0]
    choose = [[1, 2, 3, 4, 5],
             [2 ,1 ,2 ,3 ,2 ,4 ,2 ,5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i in range(len(answers)):
        for p in range(3):
            if answers[i] == choose[p][i % len(choose[p])]:
                correct[p] += 1
    maxP = max(correct)
    answer = []
    for p in range(3):
        if correct[p] == maxP:
            answer.append(p + 1)
    return answer