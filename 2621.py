card=[]
c=['R','B','Y','G']
color=dict()
number=dict()
for _ in range(5):
    tmp=input().split()
    card.append(''.join(tmp))
for i in range(5):
    color[card[i][0]]=color.get(card[i][0],0)+1
    number[card[i][1]]=number.get(card[i][1],0)+1
color=dict(sorted(color.items(),key=lambda x:-x[1]))
number=dict(sorted(number.items(),key=lambda x:(-x[1],-int(x[0]))))
color_num=list(color.values())
number_num=list(number.values())
keylist=list(number.keys())
if color_num[0]==5 and int(keylist[0])-int(keylist[-1])==4: #1
    score=int(keylist[0])+900
elif number_num==[4,1]: #2
    score=int(keylist[0])+800
elif number_num==[3,2]: #3
    score=int(keylist[0])*10+int(keylist[1])+700
elif color_num==[5]: #4
    score=int(keylist[0])+600
elif int(keylist[0])-int(keylist[-1])==4: #5
    score=int(keylist[0])+500
elif number_num[0]==3: #6
    score=int(keylist[0])+400
elif number_num[:2]==[2,2]: #7
    score=int(keylist[0])*10+int(keylist[1])+300
elif number_num[0]==2: #8
    score=int(keylist)[0]+200
else: #9
    score=int(keylist[0])+100
print(score)