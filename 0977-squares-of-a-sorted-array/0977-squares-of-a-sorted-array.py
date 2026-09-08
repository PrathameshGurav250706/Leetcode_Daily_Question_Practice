class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left=0
        right=len(nums)-1
        k=len(nums)-1
        new=[0]*len(nums)
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                new[k]=nums[left]*nums[left]
                left+=1
            else:
                new[k]=nums[right]*nums[right]
                right-=1
            k-=1
        return new
        # Time complexity: O(n)
        # Space complexity: O(1)