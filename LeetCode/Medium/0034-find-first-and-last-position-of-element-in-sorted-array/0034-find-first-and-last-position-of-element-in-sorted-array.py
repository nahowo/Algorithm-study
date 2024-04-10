class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        answer=[n,-1]
        s=0
        e=n-1
        while s<=e:
            m=(s+e)//2
            if nums[m]>=target:
                e=m-1
                if nums[m]==target:
                    answer[0]=m
            else: # nums[m]<target:
                s=m+1
        
        s=0
        e=n-1
        while s<=e:
            m=(s+e)//2
            if nums[m]<=target:
                s=m+1
                if nums[m]==target:
                    answer[1]=m
            else: # nums[m]>target:
                e=m-1
                
        if answer==[n,-1]:
            answer=[-1,-1]
            
        return answer