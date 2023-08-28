import sys
from datetime import datetime
input=sys.stdin.readline
a,b,c=map(int,input().split())
today=datetime(a,b,c)
a,b,c=map(int,input().split())
d_day=datetime(a,b,c)
time_left=(d_day-today).days
maxday=datetime((today.year+1000),today.month,today.day)
if d_day>=maxday:
    print('gg')
else:
    print('D-'+str(time_left))