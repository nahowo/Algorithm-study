class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        path=[[0]*(len(grid[0])) for _ in range(len(grid))]

        path[0][0]=grid[0][0]
            
        if len(grid[0])>1 or len(grid)>1:
            for i in range(1,len(grid[0])): # O(n)
                path[0][i]=path[0][i-1]+grid[0][i]
            for j in range(1,len(grid)): # O(n)
                path[j][0]=path[j-1][0]+grid[j][0]
            for i in range(1,len(grid)): # O(n)
                for j in range(1,len(grid[i])): # O(n)
                    path[i][j] = min(path[i-1][j], path[i][j-1])+grid[i][j]
        

        return path[len(grid)-1][len(grid[0])-1]
    
    # O(n)+O(n)+O(n)*O(n) = O(n**2)