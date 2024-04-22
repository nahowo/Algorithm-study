class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=max(nums)
        nums=set(nums)
        for i in range(m):
            if i not in nums:
                return i
        return m+1