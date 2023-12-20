class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False
        