def getSum(arr1, arr2, n, i, j):
    sum = 0
    for k in range(n):
        sum += arr1[i][k] * arr2[k][j]
    return sum

def solution(arr1, arr2):
    col = len(arr1)
    row = len(arr2[0])
    n = len(arr1[0])
    answer = [[0] * row for _ in range(col)]
    print(row, col)

    for i in range(col):
        for j in range(row):
            answer[i][j] = getSum(arr1, arr2, n, i, j)
            
    return answer