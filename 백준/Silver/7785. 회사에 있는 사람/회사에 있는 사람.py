import sys
input=sys.stdin.readline
n=int(input())
company=set()
for _ in range(n):
    person=input().split()[0]
    if person not in company:
        company.add(person)
    else:
        company.remove(person)
company=list(company)
company.sort(reverse=True)
for i in company:
    print(i)