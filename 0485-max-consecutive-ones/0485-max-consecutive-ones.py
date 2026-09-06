class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        maxC=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                maxC=max(maxC,count)
                count=0
        maxC=max(maxC,count)
                
        return maxC

        #  time complexity is O(n)
        #   space complexity is O(1)