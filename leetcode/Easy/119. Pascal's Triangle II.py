class Solution(object):
    def getRow(self, rowIndex):
        triangle = []
        for i in range(rowIndex + 1):
            row = [1]
            if i > 0:
                for j in range(1, i):
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                row.append(1)
            triangle.append(row)
        return triangle[rowIndex]
