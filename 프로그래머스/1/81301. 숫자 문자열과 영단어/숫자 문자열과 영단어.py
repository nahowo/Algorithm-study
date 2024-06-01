def solution(s):
    answer=''
    n=len(s)
    eng=['zero','one','two','three','four','five','six','seven','eight','nine']
    
    i=0
    while i<n:
        if s[i].isnumeric(): # 숫자인 경우
            answer+=s[i]
            i+=1
        else:
            for j in range(len(eng)):
                if i+len(eng[j])<=n and s[i:i+len(eng[j])]==eng[j]:
                    answer+=str(j)
                    i+=len(eng[j])
                    break
                    
    return int(answer)