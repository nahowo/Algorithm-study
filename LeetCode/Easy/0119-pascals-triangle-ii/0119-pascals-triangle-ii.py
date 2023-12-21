class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1] # 1 1
        newrow=[1]
        if rowIndex>0:
            row.append(1)
        for i in range(1,rowIndex):
            for j in range(1,i+1):
                newrow.append(row[j-1]+row[j])
            newrow.append(1)
            row=newrow.copy()
            newrow=[1]
        return row