class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky=set([-1])
        for i in range(len(arr)):
            if arr.count(arr[i])==arr[i]:
                lucky.add(arr[i])
        return max(lucky)