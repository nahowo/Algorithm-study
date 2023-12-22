class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        from math import sqrt
        prime=[True for _ in range(n)]

        if n<=1:
            return 0

        prime[0],prime[1] = False,False

        for i in range(2,int(sqrt(n))+1):
            if prime[i]:
                for j in range(i**2,n,i):
                    prime[j] = False

        return sum(prime) 