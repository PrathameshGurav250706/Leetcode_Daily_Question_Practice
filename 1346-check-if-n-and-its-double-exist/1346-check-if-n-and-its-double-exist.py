class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen=set()
        for i in arr:
            if 2*i in seen :
                return True
            if i % 2 == 0 and i // 2 in seen:
                return True
            seen.add(i)
        return False
        # Time complexity: O(n), where n is the length of arr. Each element is processed once, with O(1) average-time set lookups and insertions.

        # Space complexity: O(n) in the worst case, due to storing all distinct elements in the seen set.