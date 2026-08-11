class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)-1
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=nums[i]+prefix[i-1]
         
        for j in range(len(nums)):
            if j==0:
                if 0==prefix[n]-prefix[0]:
                    return 0
            elif  prefix[j-1]==prefix[n]-prefix[j]:
                return j
        else:
            return -1

                

        