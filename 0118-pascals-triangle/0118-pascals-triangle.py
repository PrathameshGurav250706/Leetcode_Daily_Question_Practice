class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        new=[]
        for i in range(numRows):
            row=[1]*(i+1)

            for j in range(1,i):
                row[j]=new[i-1][j-1]+new[i-1][j]
            new.append(row)
        return new