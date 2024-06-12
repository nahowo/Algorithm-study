import sys
input=sys.stdin.readline

# 1. 입력받은 문자열에서 숫자를 탐색
# 2. 숫자가 입력받은 위치에 따라 4번째 숫자를 출력

# 입력받은 문자열에서 숫자를 찾는 함수
def countStr():
    answer=0
    for i in range(3,0,-1):
        tmp=input().rstrip()
        if tmp.isnumeric():
            answer=int(tmp)+i
    
    return isFizzBuzz(answer)

# 숫자의 FizzBuzz 여부를 확인하는 함수
def isFizzBuzz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return n

print(countStr())

# 시간복잡도: O(3)