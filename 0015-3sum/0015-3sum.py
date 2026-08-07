class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        new=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1

            while l<r:
                add=nums[i] + nums[l] +nums[r]

                if add==0:
                    new.append([nums[i],nums[l],nums[r]])

                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1

                    l+=1
                    r-=1
                elif add<0:
                    l+=1
                else:
                    r-=1
                   
        return new