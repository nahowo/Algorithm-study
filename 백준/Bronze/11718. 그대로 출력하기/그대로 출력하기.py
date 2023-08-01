word=[]
while True:
    try:
        tmp=input()
    except EOFError:
        break
    word.append(tmp)
for i in word:
    print(i)