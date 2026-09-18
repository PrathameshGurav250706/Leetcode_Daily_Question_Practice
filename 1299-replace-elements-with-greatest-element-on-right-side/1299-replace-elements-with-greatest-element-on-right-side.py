class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        Max=-1
        for i in range(len(arr)-1,-1,-1):
            temp=arr[i]
            arr[i]=Max
            Max=max(Max,temp)
        return arr
        # Time complexity: O(n)
        # Space complexity: O(1)