class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={0:0,1:0,2:0}
        for i in nums:
            d[i]+=1
        
        start=0
        end=0
        for i in range(3):
            end+=d[i]
            for j in range(start,end):
                nums[j]=i
            start+=d[i]