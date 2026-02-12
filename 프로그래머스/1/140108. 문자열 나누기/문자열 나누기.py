def solution(s):
    answer = 0
    x = s[0]
    xc, nxc = 0, 0
    for i in range(len(s)):
        if s[i] == x:
            xc += 1
        else:
            nxc += 1
        if xc == nxc:
            answer += 1
            if i < len(s) - 1:
                x = s[i + 1]
                xc, nxc = 0, 0
        else:
            if i == len(s) - 1:
                answer += 1
        
    return answer