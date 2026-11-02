class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates)<=2:
            return True
        y21=coordinates[1][1]-coordinates[0][1]
        x21=coordinates[1][0]-coordinates[0][0]

        for i in range(2,len(coordinates)):
            deltay=coordinates[i][1]-coordinates[0][1]
            deltax=coordinates[i][0]-coordinates[0][0]

            if y21*deltax!=x21*deltay:
                return False
        return True