class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        global n,answer
        n=len(nums)
        answer=[]
        
        def perm(arr):
            if len(arr)==n:
                answer.append(list(arr))
                return
            for i in range(n):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    perm(arr)
                    arr.pop()
        perm([])
        return answer