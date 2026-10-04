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
        # Time complexity: O(n), where n is the length of nums. We traverse the array once to compute the product.

        # Space complexity: O(1), since we only use a constant amount of extra space (the Prod variable).