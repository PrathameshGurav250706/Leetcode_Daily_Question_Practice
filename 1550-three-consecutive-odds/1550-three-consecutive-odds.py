class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i=0
        count=0
        while i<len(arr):
            if arr[i]%2!=0:
                count+=1
                if count==3:
                    return True
            else:
                count=0
            
            i+=1
        return False
        # Time complexity: O(n), where n is the length of the input array. The loop traverses each element once.

        # Space complexity: O(1), aside from a few scalar variables (i, count), no extra data structures are used.