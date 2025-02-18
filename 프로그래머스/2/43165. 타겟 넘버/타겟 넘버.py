def dfs(num, idx, target, numbers):
    if idx == n:
        if num == target:
            return 1
        return 0
    
    return dfs(num - numbers[idx], idx + 1, target, numbers) + dfs(num + numbers[idx], idx + 1, target, numbers)

def solution(numbers, target):
    global n
    n = len(numbers)
    answer = dfs(0, 0, target, numbers)
    return answer