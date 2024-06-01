def distCheck(lpos,rpos,dest,hand):
    ldist=rdist=0
    ldist=abs(lpos[0]-dest[0])+abs(lpos[1]-dest[1])
    rdist=abs(rpos[0]-dest[0])+abs(rpos[1]-dest[1])
    if ldist<rdist:
        return "L"
    elif rdist<ldist:
        return "R"
    else:
        return hand

def solution(numbers, hand):
    if hand=='left':
        hand='L'
    else:
        hand='R'
    answer = ''
    pos={1:(0,0),2:(0,1),3:(0,2),
         4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        0:(3,1)}
    lhand=(3,0)
    rhand=(3,2)
    
    for i in numbers:
        if i==1 or i==4 or i==7:
            lhand=pos[i]
            answer+='L'
        elif i==3 or i==6 or i==9:
            rhand=pos[i]
            answer+='R'
        else:
            tmp=distCheck(lhand,rhand,pos[i],hand)
            answer+=tmp
            if tmp=='L':
                lhand=pos[i]
            else:
                rhand=pos[i]
    
    return answer