N, X = map(int, input().split())

if N > X or N * 26 < X:
    print('!')
else:
    string_list = ['A'] * N
    X -= N
    i = N - 1

    while X > 0:
        if X >= 25:
            string_list[i] = 'Z'
            i -= 1
            X -= 25
        else:
            string_list[i] = chr(X + 65)
            break
            
    print(''.join(string_list))