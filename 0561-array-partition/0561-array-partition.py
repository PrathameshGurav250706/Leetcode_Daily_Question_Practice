class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # i=0
        # Total=0
        # while i<len(nums):
        #     Total+=nums[i]
        #     i+=2
        # return Total
        # - Time complexity: Sorting dominates at O(n log n). The subsequent loop runs about n/2 steps, which is O(n). Overall, O(n log n).
        # - Space complexity: Sorting in place uses O(1) extra space beyond the input list, so the auxiliary space is O(1). If the sorting algorithm is not in-place, it could be O(n) additional space, but assuming typical in-place sort, it's O(1).

        nums.sort()
        return sum(nums[::2])
        # - Time complexity: Dominated by sorting, which is O(n log n) for n = len(nums). The slicing nums[::2] and summing across about n/2 elements take O(n) time, but O(n log n) from sorting dominates. Overall O(n log n).

        # - Space complexity: Sorting in Python uses O(n) additional space in the worst case (Timsort requires temporary space). The sum over the sliced view uses O(1) extra space aside from the iteration variables. Overall O(n) auxiliary space in the worst case. If the sort is in-place (not always applicable in Python’s Timsort with extra space), the extra space could be O(1) amortized, but typical implementation is O(n).