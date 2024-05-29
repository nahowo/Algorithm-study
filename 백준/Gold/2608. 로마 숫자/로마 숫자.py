import sys
from collections import deque
input=sys.stdin.readline
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
   'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
arr=list(d.items())
arr.sort(key=lambda x:x[1],reverse=True)

def romeToInt(s):
    l=len(s)
    i=0
    number=0
    while i<l:
        if i==l-1:
            number+=d[s[i]]
            break
        if d[s[i]]>=d[s[i+1]]: # 큰 숫자-작은 숫자인 경우
            number+=d[s[i]]
            i+=1
        else: # 작은 숫자-큰 숫자인 경우
            number+=d[s[i:i+2]]
            i+=2
    return number

def intToRome(itg):
    i=0
    number=deque()
    check1={'V','L','D'} # V,L,D 사용 여부 체크
    check2={'I','X','C','M'}
    check3={'IV','IX','XL','XC','CD','CM'}
    while i<len(arr):
        if itg>=arr[i][1]:
            if arr[i][0] in check1: # V,L,D
                number.append(arr[i][0])
                check1.remove(arr[i][0])
                itg-=arr[i][1]

            elif arr[i][0] in check2: # I,X,C,M
                if len(number)>=3: # 이전 3개 문자 확인
                    if number[-1]==arr[i][0] and number[-2]==arr[i][0] and number[-3]==arr[i][0]:
                        i+=1
                        continue
                number.append(arr[i][0])
                itg-=arr[i][1]
            
            elif arr[i][0] in check3: # IV,IX,XL,XC,CD,CM
                if len(number)>=1:
                    if (arr[i][0]=='IV' and number[-1]=='IX') or (arr[i][0]=='IX' and number[-1]=='IV'):
                        i+=1
                        continue
                    elif (arr[i][0]=='XL' and number[-1]=='XC') or (arr[i][0]=='XC' and number[-1]=='XL'):
                        i+=1
                        continue
                    elif (arr[i][0]=='CD' and number[-1]=='CM') or (arr[i][0]=='CM' and number[-1]=='CD'):
                        i+=1
                        continue
                number.append(arr[i][0])
                check3.remove(arr[i][0])
                itg-=arr[i][1]
        else:
            i+=1
    return ''.join(number)

rome1=input().rstrip()
rome2=input().rstrip()
i1=romeToInt(rome1)
i2=romeToInt(rome2)
print(i1+i2)
print(intToRome(i1+i2))