class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[[1] for _ in range(numRows)]
        if numRows>1:
            triangle[1].append(1)
        for i in range(2,numRows):
            for j in range(1,i):
                triangle[i].append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle[i].append(1)
        return triangle