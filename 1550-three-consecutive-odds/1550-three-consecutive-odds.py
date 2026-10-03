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
            else:
                count=0
            if count==3:
                return True
            i+=1
        return False
        