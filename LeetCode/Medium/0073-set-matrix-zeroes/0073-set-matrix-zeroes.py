class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colset=set()
        rowset=set()
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    colset.add(i)
                    rowset.add(j)
        
        for i in colset:
            matrix[i]=[0]*n
            
        for i in range(m):
            for j in rowset:
                matrix[i][j]=0