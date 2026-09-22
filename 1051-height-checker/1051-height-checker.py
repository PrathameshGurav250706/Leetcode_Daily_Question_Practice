class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        new=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=new[i]:
                count+=1
        return count

        # - Time complexity: O(n log n) due to sorting, where n is the length of heights. The subsequent scan is O(n), so overall O(n log n).
        # - Space complexity: O(n) extra space for the sorted copy new (since sorted creates a new list). If sorting is in-place (not the case here), could be O(1) auxiliary space.