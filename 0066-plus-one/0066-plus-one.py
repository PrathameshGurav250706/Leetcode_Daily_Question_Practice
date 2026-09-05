class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Time complexity: O(n),
        # Space complexity: O(n)
        new=0
        for i in digits:
            new=new*10+i
        new=new+1
        seen=[]
        for j in str(new):
            seen.append(int(j))
        return seen    