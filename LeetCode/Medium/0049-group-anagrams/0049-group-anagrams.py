class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for i in strs:
            tmp=str(sorted(i))
            d[tmp]=d.get(tmp,[])+[i]
        answer=list(d.values())
        return answer