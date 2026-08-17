class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen=set()
        duplicate=0
        for num in nums:
            if num in seen:
                duplicate=num
            seen.add(num)
        missing=0
        for i in range(1,len(nums)+1):
            if i not in nums:
                missing=i
        return [duplicate,missing]