class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        # Time complexity: O(n)
        # Space complexity: O(1)


        # for k in nums:
        #     if k==0:
        #         nums.remove(0)
        #         nums.append(0)
        # time complexity degrades to O(n^2) in the worst case.
        # Space complexity: O(1)
            