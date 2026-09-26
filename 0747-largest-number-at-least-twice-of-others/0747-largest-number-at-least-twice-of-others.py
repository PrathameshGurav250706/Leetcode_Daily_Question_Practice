class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new=sorted(nums)
        if new[-1]>=(2*new[-2]):
            return nums.index(new[-1])
        return -1

        # This code sorts the input list, which takes O(n log n) time and O(n) extra space for the sort.