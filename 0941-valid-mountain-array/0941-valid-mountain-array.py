class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        start=0
        
        Max_ind=arr.index(max(arr))

        # Peak cannot be at either end
        if Max_ind == 0 or Max_ind == len(arr) - 1:
            return False
        
        for i in range(1,Max_ind+1):
            if arr[i]>arr[i-1]:
                start+=1

        for i in range(Max_ind+1,len(arr)):
            if arr[i]<arr[i-1]:
                start+=1

        if start==len(arr)-1:
            return True
        return False