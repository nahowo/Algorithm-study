class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=dict()
        M=(10**5)+1
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                d[s[i]]=M
        char=list(d.values())
        answer=min(char)
        if answer==M:
            return -1
        else:
            return answer