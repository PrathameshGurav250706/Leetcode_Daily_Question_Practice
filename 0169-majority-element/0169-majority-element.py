class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fre={}
        n=len(nums)
        for num in nums:
            if num in fre:
                fre[num]=fre[num]+1
            else:
                fre[num]=1
        for key in fre.keys():
            if fre[key]>n/2:
                return key