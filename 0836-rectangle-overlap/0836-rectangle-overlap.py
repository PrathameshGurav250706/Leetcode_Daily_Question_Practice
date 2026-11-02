class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        r1x1=rec1[0]
        r1y1=rec1[1]
        r1x2=rec1[2]
        r1y2=rec1[3]

        r2x1=rec2[0]
        r2y1=rec2[1]
        r2x2=rec2[2]
        r2y2=rec2[3]

        if r2x1>=r1x2:
            return False
        if r2y1>=r1y2:
            return False
        if r1x1>=r2x2:
            return False
        if r1y1>=r2y2:
            return False
        return True
        # Time complexity: O(1) since it performs a fixed number of arithmetic and comparison operations regardless of input size.

        # Space complexity: O(1) since it uses a constant amount of extra space.