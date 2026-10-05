class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Single=0
        double=0
        for i in nums:
            if i>9:
                Single+=i
            else:
                double+=i
        if Single>double or double>Single:
            return True
        return False
