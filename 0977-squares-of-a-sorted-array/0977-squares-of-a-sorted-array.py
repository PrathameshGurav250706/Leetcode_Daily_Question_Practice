class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0 
        right = len(nums) - 1
        while left <= right:
            nums[left] = nums[left]*nums[left]
            left = left + 1

        nums.sort()
        return nums
        