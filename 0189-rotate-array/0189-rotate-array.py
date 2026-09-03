class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        def rotate(start,end):
            while start<=end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        
        if k%n==0:
            return
        k=k%n
        rotate(0,n-1)       #first rotate all list
        rotate(0,k-1)        #rotate first k elements
        rotate(k,n-1)       #rotate remaning elements

        

            
        