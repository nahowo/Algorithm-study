class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer=0
        i=5
        while i<=n:
            answer+=n//i
            i*=5
        return answer