class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i==sum([int(k) for k in str(nums[i])]):
                return i
        return -1