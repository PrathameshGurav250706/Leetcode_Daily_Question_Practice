class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        seen = set()
        currentSum = 0
        maxSum = 0
        left = 0

        for right in range(len(nums)):

            # If duplicate comes, remove elements from left
            while nums[right] in seen:
                seen.remove(nums[left])
                currentSum -= nums[left]
                left += 1

            seen.add(nums[right])
            currentSum += nums[right]

            # Keep window size at most k
            if right - left + 1 > k:
                seen.remove(nums[left])
                currentSum -= nums[left]
                left += 1

            # Only consider windows of exactly k elements
            if right - left + 1 == k:
                maxSum = max(maxSum, currentSum)

        return maxSum