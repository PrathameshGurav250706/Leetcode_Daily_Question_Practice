class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # left=0
        # right=len(nums)-1

        # while left<right:
        #     if nums[left]%2!=0 and nums[right]%2==0:
        #         nums[left],nums[right]=nums[right],nums[left]

        #     if nums[left]%2==0:
        #         left+=1

        #     if nums[right]%2!=0:
        #         right-=1
        # return nums

        # Time complexity: O(n) because each element is inspected a constant number of times as the pointers move toward each other. In the worst case, each element is swapped at most once, and the loop runs about n iterations.

        # Space complexity: O(1) extra space, besides the input array, since it uses a constant number of additional variables (left, right). The operation is in-place.

        start=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[start],nums[i]=nums[i],nums[start]
                start+=1
        return nums

        # Time complexity: O(n), where n is the length of nums. Each element is inspected once, and each swap is O(1).

        # Space complexity: O(1) extra space, since the operation is in-place and uses only a couple of indice