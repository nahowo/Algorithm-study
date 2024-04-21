class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        q=deque()
        for i in range(len(nums)):
            if nums[i]==0:
                q.append(i)
            else:
                if len(q)>0:
                    x=q.popleft()
                    nums[i],nums[x]=nums[x],nums[i]
                    q.append(i)