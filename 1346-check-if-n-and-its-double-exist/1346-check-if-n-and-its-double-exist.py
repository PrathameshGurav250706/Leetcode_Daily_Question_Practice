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
