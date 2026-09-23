class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

#         Time complexity:
# - Finding the index of the maximum element is O(n).
# - The two subsequent linear scans across the array together examine each element once, contributing O(n).
# - Overall time complexity: O(n).

# Space complexity:
# - Uses a constant amount of extra space (a few integer variables), so O(1) auxiliary space

        # start=0
        
        # Max_ind=arr.index(max(arr))

        # # Peak cannot be at either end
        # if Max_ind == 0 or Max_ind == len(arr) - 1:
        #     return False
        
        # for i in range(1,Max_ind+1):
        #     if arr[i]>arr[i-1]:
        #         start+=1

        # for i in range(Max_ind+1,len(arr)):
        #     if arr[i]<arr[i-1]:
        #         start+=1

        # if start==len(arr)-1:
        #     return True
        # return False

        i=0
        n=len(arr)
        while i+1<n and arr[i+1]>arr[i]:
            i+=1

        if i == 0 or i == len(arr)-1:
            return False

        while i+1<n and arr[i]>arr[i+1]:
            i+=1

        if i==len(arr)-1:
            return True
        return False

#         Time complexity:
# - The first while loop advances i while the sequence is strictly increasing from the start. In the worst case it traverses up to n-1 elements.
# - The second while loop continues from that peak while the sequence is strictly decreasing. In the worst case it traverses the remaining elements.
# - Overall, each element is visited at most once, so the time complexity is O(n).

# Space complexity:
# - The algorithm uses a constant amount of extra space (a few integers: i and n). No additional data structures are allocated.
# - Therefore, the space complexity is O(1).