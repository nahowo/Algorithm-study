def isRight(s):
    stack = []
    
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if stack:
                if stack and (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                     stack.append(i)
            else:
                stack.append(i)

    if not stack:
        return 1
    return 0

def rotate(s):
    return s[1:] + s[0]

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += isRight(s)
        s = rotate(s)
    
    return answer