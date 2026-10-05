class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        data={}
        for i in moves:
            data[i]=data.get(i,0)+1
        if (data.get("R", 0) == data.get("L", 0) and
            data.get("U", 0) == data.get("D", 0)):
            return True
        return False
        # Time complexity: O(n), where n is the length of the moves string. The loop iterates once over all characters. Constant-time dictionary operations are used for counting.

        # Space complexity: O(1) extra space, since the dictionary stores at most a fixed set of keys (R, L, U, D), i.e., a constant amount of space regardless of input length.