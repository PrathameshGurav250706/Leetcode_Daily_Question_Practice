class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        firstSum=sum(nums[:k])
        maxSum=firstSum
        for i in range(k,len(nums)):
            firstSum=firstSum-nums[i-k]+nums[i]
            maxSum=max(maxSum,firstSum)
        k = float(k)
        return maxSum / k