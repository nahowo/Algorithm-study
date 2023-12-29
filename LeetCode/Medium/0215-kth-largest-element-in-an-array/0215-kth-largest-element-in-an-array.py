class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # solution without sorting
        
        import heapq
        
        for i in range(len(nums)): # O(n)
            nums[i]=-nums[i]
        heapq.heapify(nums) # O(n)
        for i in range(k): # O(n)
            kth=heapq.heappop(nums) # O(logn)
        return -kth
        
        # O(nlogn) + O(n) + O(n)