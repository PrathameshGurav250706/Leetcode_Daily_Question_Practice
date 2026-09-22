class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new=list(set(nums))
        new.sort()
        if len(new)>=3:
            return new[-3]
        else:
            return new[-1]
