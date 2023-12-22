class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort() # O(nlogn)
        return nums[-k] # O(n)
        
        # O(nlogn)+O(n) = O(nlogn)