import sys
sys.setrecursionlimit(10 ** 4)

def reverse(u):
    ret = ''
    for i in u[1 : len(u) - 1]:
        if i == '(':
            ret += ')'
        else:
            ret += '('
    return ret

def solution(p):
    answer = ''
    
    while p:
        u = ''
        cnt = 0
        flag = False
        l = 0
        for i in p:
            if i == '(':
                cnt += 1
                u += i
            else:
                cnt -= 1
                if cnt < 0:
                    flag = True
                u += i
            l += 1 # 자른 길이
            if cnt == 0:
                p = p[l:]
                if not flag:
                    answer += u + solution(p)
                    return answer
                else: # 올바르지 않은 괄호
                    nu = '(' + solution(p) + ')'
                    answer += nu + reverse(u)
                    return answer
        
    return answer