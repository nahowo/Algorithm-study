import sys
input = sys.stdin.readline

def bnp(money):
    cnt = 0
    for i in range(3, 17):
        canBuy = money // price[i]
        cnt += canBuy
        money -= price[i] * canBuy
    return money, cnt

def timing(money):
    cnt = 0
    for i in range(3, 17):
        if price[i - 3] > price[i - 2] > price[i - 1]:
            canbuy = money // price[i]
            cnt += canbuy
            money -= price[i] * canbuy
        if price[i - 3] < price[i - 2] < price[i - 1]:
            money += price[i] * cnt
            cnt = 0
    return money, cnt

def solution():
    global price
    money = int(input())
    price = list(map(int, input().split()))
    price = [price[0], price[0], price[0]] + price
    bnpMoney, bnpCnt = bnp(money)
    timingMoney, timingCnt = timing(money)
    bnpRet = bnpMoney + bnpCnt * price[16]
    timingRet = timingMoney + timingCnt * price[16]

    answer = "SAMESAME"
    if bnpRet > timingRet:
        answer = "BNP"
    elif bnpRet < timingRet:
        answer = "TIMING"
    return answer
    
print(solution())