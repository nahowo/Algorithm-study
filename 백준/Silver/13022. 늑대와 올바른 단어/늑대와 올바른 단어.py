import sys
input=sys.stdin.readline
w=['o','l','f']
word=input().rstrip()
def func(word):
    try:
        while word!='':
            n=0
            if word[0]=='w':
                while word[0]!='o':
                    n+=1
                    word=word[1:]
                for i in w:
                    if word[:n]==i*n:
                        word=word[n:]
                    else:
                        return 0
            else:
                return 0
        return 1
    except:
        return 0
print(func(word))