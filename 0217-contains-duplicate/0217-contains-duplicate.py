class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time complexity: O(n)
        # Space complexity: O(n) in the worst case, since in the case with no duplicates the entire set seen will store all elements.
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False