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
        else:
            return False
        # the code iterates through the list nums once, performing O(1) work per element. Let n be the length of nums. Time complexity is O(n). It uses a constant amount of additional space (a few integer counters), so space complexity is O(1). The final conditional is O(1) as well.