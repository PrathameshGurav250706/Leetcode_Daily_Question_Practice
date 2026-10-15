class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add=0
        for i in range(len(nums)):
            new=set()
            for j in range(i,len(nums)):
                new.add(nums[j])
                add+=len(new)*len(new)
        return add

            

