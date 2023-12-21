class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky = set()
        for num in set(arr):
            if arr.count(num) == num:
                lucky.add(num)
        if len(lucky) > 0:
            return max(lucky)
        else:
            return -1