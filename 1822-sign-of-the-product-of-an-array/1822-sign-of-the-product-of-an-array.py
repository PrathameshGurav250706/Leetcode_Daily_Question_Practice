class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Prod=1
        for i in nums:
            Prod*=i
        if Prod>0:
            return 1
        if Prod==0:
            return 0
        else:
            return -1
