class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check=set()
        for i in nums:
            if i in check:
                check.remove(i)
            else:
                check.add(i)
        
        singleNumber=list(check)[0]
        return singleNumber