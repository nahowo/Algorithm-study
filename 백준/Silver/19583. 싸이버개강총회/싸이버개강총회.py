import sys
input=sys.stdin.readline
s,e,q=input().rstrip().split()
s=int(s.replace(":",""))
e=int(e.replace(":",""))
q=int(q.replace(":",""))
before_party=set()
after_party=set()
while True:
    checked=0
    try:
        time,person=input().rstrip().split()
        time=int(time.replace(":",""))
    except:
        break
    if time<=s:
        before_party.add(person)
    elif e<=time<=q:
        after_party.add(person)
print(len(before_party&after_party))