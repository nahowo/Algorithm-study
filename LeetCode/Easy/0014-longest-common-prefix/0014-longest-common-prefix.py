class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=""
        n=len(strs)
        m=200
        for i in strs:
            m =min(m,len(i))
            
        for j in range(m):
            cnt = 0
            for i in range(n):
                if strs[0][j] ==strs[i][j]:
                    cnt +=1
            if cnt == n:
                answer += strs[0][j]
            else:
                return answer
        return answer