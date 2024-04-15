class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        d=dict()
        for i in range(len(intervals)):
            d[i+1]=intervals[i]
        
        nums=[0]*(10001)
        for i in range(len(intervals)):
            s=i+1
            for j in range(intervals[i][0],intervals[i][1]+1):
                if nums[j]!=0:
                    k=nums[j]
                    s=k
                    d[k]=[min(d[k][0],intervals[i][0]),max(d[k][1],intervals[i][1])]
            for j in range(intervals[i][0],intervals[i][1]+1):
                nums[j]=s
        
        nums.append(0)
        answer=[]
        k=0
        for i in range(10002):
            if nums[k]==0 and nums[i]!=0:
                k=i
            elif nums[k]!=nums[i]:
                answer.append([k,i-1])
                k=i
        return answer