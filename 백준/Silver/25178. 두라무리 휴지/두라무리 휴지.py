import sys
input = sys.stdin.readline

def solution():
    global n
    n = int(input())
    str1 = input().rstrip()
    str2 = input().rstrip()

    if canRearrange(str1, str2) and sameFirstLast(str1, str2) and sameWithoutVowel(str1, str2):
        return "YES"
    return "NO"

def canRearrange(s1, s2):
    d1 = sorted(list(parseStr(s1).items()))
    d2 = sorted(list(parseStr(s2).items()))
    for i in range(len(d1)):
        if d1[i][0] != d2[i][0] or d1[i][1] != d2[i][1]:
            return False
    return True

def parseStr(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

def sameFirstLast(s1, s2):
    if s1[0] == s2[0] and s1[n - 1] == s2[n - 1]:
        return True
    return False

def sameWithoutVowel(s1, s2):
    s1 = removeVowel(s1)
    s2 = removeVowel(s2)
    if s1 == s2:
        return True
    return False

def removeVowel(s):
    ret = ""
    vowel = {'a', 'e', 'i', 'o', 'u'}
    for i in s:
        if i not in vowel:
            ret += i
    return ret

print(solution())