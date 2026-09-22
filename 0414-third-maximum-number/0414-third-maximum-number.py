class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new=list(set(nums))
        new.sort()
        if len(new)>=3:
            return new[-3]
        else:
            return new[-1]
            
        # Time complexity: O(n log n) in the worst case due to removing duplicates (set) and sorting the resulting list. Specifically, building the set is O(n) on average, and sorting the at most n elements is O(n log n). Overall O(n log n).

        # Space complexity: O(n) for storing the unique elements in the set (and the resulting list). In the worst case, all elements are unique.