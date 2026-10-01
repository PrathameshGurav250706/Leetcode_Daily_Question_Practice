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
        # Time complexity: O(n * d) where n is the length of nums and d is the number of digits in the largest number (on average constant for typical constraints, since digits are small). In worst case, if nums contains numbers with up to k digits, it becomes O(nk).

        # Space complexity: O(1) extra space (besides the input list), since it uses a few scalar variables (total, add) and no auxiliary data structures.