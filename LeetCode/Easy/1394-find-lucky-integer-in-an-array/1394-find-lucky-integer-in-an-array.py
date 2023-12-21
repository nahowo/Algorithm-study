class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky=set([-1])
        for i in set(arr):
            if arr.count(i)==i:
                lucky.add(i)
        return max(lucky)