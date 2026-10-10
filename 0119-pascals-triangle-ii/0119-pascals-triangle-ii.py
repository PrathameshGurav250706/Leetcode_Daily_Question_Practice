class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        new=[]
        for i in range(rowIndex+1):
            row=[1]*(i+1)

            for j in range(1,i):
                row[j]=new[i-1][j-1]+new[i-1][j]
            new.append(row)
        return new[rowIndex]
        # - Time complexity: O(rowIndex^2)
        # Each row i (0-based) has i+1 elements, and computing inner values runs in O(i) for each row, plus the final row construction. Summing i from 0 to rowIndex gives O((rowIndex+1) rowIndex / 2) = O(rowIndex^2).

        # - Space complexity: O(rowIndex^2) time, but specifically extra space besides output is O(rowIndex^2) because it stores all rows in new (a list of lists). The final returned row is of length rowIndex+1, but intermediate storage new contains all previous rows, totaling about (rowIndex+1)(rowIndex+2)/2 elements. If only the final row were needed, the space could be reduced to O(rowIndex)