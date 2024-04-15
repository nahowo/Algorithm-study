class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervals.sort()

        stack=[]
        for i in intervals:
            if len(stack)==0:
                stack.append(i)
            else:
                if stack[-1][1]>=i[0]:
                    stack[-1]=[stack[-1][0],max(stack[-1][1],i[1])]
                else:
                    stack.append(i)
        return stack