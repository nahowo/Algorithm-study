import sys
input=sys.stdin.readline

def func():
    n=int(input())
    global tree
    tree=dict()
    for _ in range(n):
        a,b,c=input().split()
        tree[a]=[b,c]
        
    global preAnswer,inAnswer,postAnswer
    preAnswer=[]
    inAnswer=[]
    postAnswer=[]

    preorder('A')
    inorder('A')
    postorder('A')

    print(''.join(preAnswer))
    print(''.join(inAnswer))
    print(''.join(postAnswer))
    
def preorder(now): # 전위 순회: root -> left -> right
    if now=='.':
        return
    preAnswer.append(now)
    preorder(tree[now][0])
    preorder(tree[now][1])

def inorder(now): # 중위 순회: left -> root -> right
    if now=='.':
        return
    inorder(tree[now][0])
    inAnswer.append(now)
    inorder(tree[now][1])

def postorder(now): # 후위 순회: left -> right -> root
    if now=='.':
        return
    postorder(tree[now][0])
    postorder(tree[now][1])
    postAnswer.append(now)

func()