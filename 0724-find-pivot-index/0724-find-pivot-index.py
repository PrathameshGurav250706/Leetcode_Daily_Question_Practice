class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        total=sum(nums)
        for i in range(len(nums)):
            right=total-left-nums[i]
            if left==right:
                return i
            
            left=left+nums[i]
        return -1
        # Time complexity: O(n), where n is the length of nums. The loop traverses the array once, and each iteration does O(1) work (constant-time arithmetic).

        # Space complexity: O(1), aside from a few scalar variables (left, total, right). No extra data structures are used.