import sys
input=sys.stdin.readline

def func():
    s=input().rstrip()
    cnt={'P':13,'K':13,'H':13,'T':13}
    cardset=set()
    for i in range(0,len(s)-2,3):
        if s[i:i+3] in cardset:
            print("GRESKA")
            return
        else:
            cardset.add(s[i:i+3])
        
        cnt[s[i]]-=1
    
    print(*list(cnt.values()))
    return

func()