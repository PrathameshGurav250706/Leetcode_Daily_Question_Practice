class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Time complexity: O(n^2)
        # # Space complexity: O(1)
        # for i in nums:
        #     if nums.count(i)==1:
        #         return i
        
        # Time complexity: O(n)
        # Space complexity: O(1)
        d=0
        for i in nums:
            d=i^d           #XOR 

        return d