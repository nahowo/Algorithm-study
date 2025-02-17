ALPHA = ['A', 'E', 'I', 'O', 'U']

def dfs(w, l):
    if l == 5:
        return
    
    for i in range(5):
        dictionary.append(w + ALPHA[i])
        dfs(w + ALPHA[i], l + 1)

def solution(word):
    global dictionary
    dictionary = []
    dfs('', 0)
    answer = dictionary.index(word) + 1
    return answer