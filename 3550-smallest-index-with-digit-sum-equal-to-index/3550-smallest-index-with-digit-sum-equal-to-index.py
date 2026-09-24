class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if i==sum([int(k) for k in str(nums[i])]):
        #         return i
        # return -1

        for i in range(len(nums)):
            count=0
            while nums[i]>0:
                digit=nums[i]%10
                count+=digit
                nums[i]=nums[i]//10
            if i==count:
                return i
        return -1