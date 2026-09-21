class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=set(nums)
        data=[]
        for i in range(1,len(nums)+1):
            if i not in new:
                data.append(i)
        return data