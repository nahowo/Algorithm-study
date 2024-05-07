# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s =1
        e =n
        answer =n

        while s<=e:
            m = int((s+e)/2)
            if not isBadVersion(m):
                s=m+1
            else:
                e=m-1
                answer=m
                
        return answer