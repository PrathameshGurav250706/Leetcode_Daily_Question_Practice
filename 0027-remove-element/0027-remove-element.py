class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left=0
        for right in range(len(nums)):
            if nums[right]!=val:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return left
        # Time complexity: O(n), where n is the length of nums. The loop visits each element once.

        # Space complexity: O(1) extra space, since it uses a few indices and swaps in place.