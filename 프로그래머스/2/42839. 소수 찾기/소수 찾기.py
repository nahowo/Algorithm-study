def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** (1 / 2)) + 2):
        if n % i == 0 and n != i:
            return False
    return True

def bruteForce(maxL, visited, num, numbers):
    global answer
    if len(num) == maxL:
        if isPrime(int(num)):
            answer.add(int(num))
            return
        return
    
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            bruteForce(maxL, visited, num + numbers[i], numbers)
            visited[i] = False
    return

def solution(numbers):
    global answer
    answer = set()
    
    for i in range(1, len(numbers) + 1):
        visited = [False] * len(numbers)
        bruteForce(i, visited, "", numbers)
    return len(answer)