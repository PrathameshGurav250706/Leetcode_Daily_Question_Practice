class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        add=0
        for i in nums:
            while i>0:
                digit=i%10
                add=add+digit
                i=i//10

        return total-add