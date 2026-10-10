class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        Total=0
        while i<len(nums):
            Total+=nums[i]
            i+=2
        return Total