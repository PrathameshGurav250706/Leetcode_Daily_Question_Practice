class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        s=set(nums)

        setSum=sum(s)
        actualSum=sum(nums)
        expectedSum=(n*(n+1))//2

        duplicate=actualSum-setSum
        missing=expectedSum-setSum

        return [duplicate,missing]

