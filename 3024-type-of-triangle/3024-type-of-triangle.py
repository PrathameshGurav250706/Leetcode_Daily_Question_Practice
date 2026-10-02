class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if (nums[0] + nums[1] <= nums[2] or
            nums[0] + nums[2] <= nums[1] or
            nums[1] + nums[2] <= nums[0]):
            return "none"

        if nums[0]==nums[1]==nums[2]:
            return "equilateral"
        elif nums[0]==nums[1] or nums[0]==nums[2] or nums[1]==nums[2]:
            return "isosceles"
        else:
            return "scalene"

        # Time complexity: O(1) because it performs a constant number of arithmetic and comparison operations on three elements, regardless of input size.

        # Space complexity: O(1) since it uses a constant amount of additional space.