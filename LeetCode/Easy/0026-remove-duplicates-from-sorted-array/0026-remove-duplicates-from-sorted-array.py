class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        check=[False]*201
        for i in nums:
            i+=100
            if not check[i]:
                nums[k]=i-100
                k+=1
                check[i]=True
        return k