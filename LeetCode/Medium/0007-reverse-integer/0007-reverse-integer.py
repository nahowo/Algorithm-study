class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            newx=str(x)[::-1] #O(31)
            newx=int(newx) #O(31)
            if newx>(2**31)-1:
                newx=0
        else:
            newx=str(x)[1:][::-1] #O(31)+O(31)
            newx=int(newx)*-1 #O(31)
            if newx<-(2**31):
                newx=0
        return newx
    
    # 양수일 경우 2*O(31)
    # 음수일 경우 3*O(31)