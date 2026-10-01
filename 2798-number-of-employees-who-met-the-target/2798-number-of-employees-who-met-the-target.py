class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        for i in hours:
            if i>=target:
                count+=1
        return count
        # Time complexity: O(n), where n is the length of the hours list. The loop iterates once over all elements.

        # Space complexity: O(1), since only a few scalar variables are used (count). No extra data structures are allocated proportional to input size.