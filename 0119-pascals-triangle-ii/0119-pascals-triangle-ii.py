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
        