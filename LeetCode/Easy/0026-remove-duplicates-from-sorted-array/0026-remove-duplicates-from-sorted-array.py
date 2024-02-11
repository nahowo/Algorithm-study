class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while True:
            try:
                if nums[i]!=nums[i+1]:
                    i+=1
                else:
                    nums.remove(nums[i])
            except IndexError:
                break
        k=len(nums)
        return k