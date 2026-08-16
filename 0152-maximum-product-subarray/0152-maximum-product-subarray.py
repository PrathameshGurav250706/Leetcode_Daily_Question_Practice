class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preffix=1
        suffix=1
        ans=float('-inf')
        for i in range(len(nums)):
            if preffix==0:
                preffix=1
            if suffix==0:
                suffix=1
            preffix*=nums[i]
            suffix*=nums[len(nums)-i-1]
            ans=max(ans,preffix,suffix)
        return ans