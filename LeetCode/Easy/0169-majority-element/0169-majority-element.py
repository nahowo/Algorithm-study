class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=dict()
        tmax=nums[0]
        for i in nums:
            count[i]=count.get(i,0)+1
            if count.get(i)>count.get(tmax):
                tmax=i
        return tmax