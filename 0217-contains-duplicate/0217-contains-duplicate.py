class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time complexity: O(n)
        # Space complexity: O(n)
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False