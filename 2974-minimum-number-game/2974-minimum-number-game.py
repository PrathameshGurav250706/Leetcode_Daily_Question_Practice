class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        nums.sort()
        while  len(nums)>0:
            new.append(nums.pop(1))
            new.append(nums.pop(0))
        return new
        # - Time complexity: O(n^2) in the worst case, because each iteration pops from the front and then from index 1, which are O(n) operations on the list, and this repeats roughly n/2 times.
        # - Space complexity: O(n) for the new list that stores all elements, plus O(1) extra space aside from the output.