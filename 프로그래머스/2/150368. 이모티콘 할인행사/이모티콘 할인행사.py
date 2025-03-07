from itertools import product

def solution(users, emoticons):
    def calc(user, perc, emoticons):
        amount = 0
        for i in range(len(perc)):
            if perc[i] >= user[0]:
                amount += emoticons[i] * (100 - perc[i]) / 100
            if amount >= user[1]:
                return 0, True
        return amount, False
    
    global percentage
    answer = [0, 0]
    percentage = [10, 20, 30, 40]
    u = len(users)
    n = len(emoticons)
    
    for perc in product(percentage, repeat = n):
        totalM = 0
        tmp = 0
        for i in range(u):
            money, flag = calc(users[i], perc, emoticons)
            if flag:
                tmp += 1
            totalM += money
        if answer[0] < tmp or (answer[0] == tmp and answer[1] < totalM):
            answer[0], answer[1] = tmp, totalM
    
    return answer