import sys
input=sys.stdin.readline

def main():
    m=int(input())
    s=0 # 집합 초기화
    a=(1<<21)-1 # 1~20까지의 원소가 들어있는 집합

    for i in range(m):
        cmd=input().rstrip().split()
        if cmd[0]=='all':
            s=a
        elif cmd[0]=='empty':
            s=0
        elif cmd[0]=='add':
            s=(1<<(20-int(cmd[1])))|s
        elif cmd[0]=='remove':
            s=~(1<<(20-int(cmd[1])))&s
        elif cmd[0]=='toggle':
            s=(1<<(20-int(cmd[1])))^s
        elif cmd[0]=='check':
            print(int(bool((1<<(20-int(cmd[1])))&s)))

main()