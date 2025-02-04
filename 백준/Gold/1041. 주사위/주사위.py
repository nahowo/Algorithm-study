import sys
input = sys.stdin.readline
three = [[0, 1, 2], [0, 1, 3], [0, 2, 4], [0, 3, 4], 
         [5, 1, 2], [5, 1, 3], [5, 2, 4], [5, 3, 4]]

def solution():
    n = int(input())
    numbers = list(map(int, input().split()))
    if n == 1:
        return sum(numbers) - max(numbers)
    threeSide = 4
    twoSide = 8 * n - 12
    oneSide = 5 * (n ** 2) - 16 * n + 12

    minThree = sum(numbers)
    for t in three:
        tmpSum = numbers[t[0]] + numbers[t[1]] + numbers[t[2]]
        minThree = min(minThree, tmpSum)
    
    minTwo = sum(numbers)
    for i in range(6):
        for j in range(i + 1, 6):
            if i + j == 5:
                continue
            tmpSum = numbers[i] + numbers[j]
            minTwo = min(minTwo, tmpSum)
    
    return threeSide * minThree + twoSide * minTwo + oneSide * min(numbers)

print(solution())