class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by=[[] for _ in range(n+1)]
        judge_candidate=set(range(1,n+1)) # 다른 사람을 믿지 않는 사람
        for i in range(len(trust)):
            trusted_by[trust[i][1]].append(trust[i][0])
            if trust[i][0] in judge_candidate:
                judge_candidate.remove(trust[i][0])
        judge_candidate=list(judge_candidate)
        for i in judge_candidate:
            if len(trusted_by[i])==n-1:
                return i
        return -1