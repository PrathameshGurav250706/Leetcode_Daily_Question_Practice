class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        add=0
        for i in nums:
            for j in str(i):
                add=add+int(j)
        return total-add