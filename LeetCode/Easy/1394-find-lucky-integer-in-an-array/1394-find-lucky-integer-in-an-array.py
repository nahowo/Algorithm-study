class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d=dict()
        lucky=-1
        
        for i in range(len(arr)):
            d[arr[i]]=d.get(arr[i],0)+1
        
        for i,j in d.items():
            if i==j:
                if lucky<i:
                    lucky=i
        return lucky