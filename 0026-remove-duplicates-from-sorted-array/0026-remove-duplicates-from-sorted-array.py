class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j
        # Time complexity: O(n), where n is the length of nums. The loop traverses the array once.

        # Space complexity: O(1) extra space. The operation is in-place, using a few scalar variables