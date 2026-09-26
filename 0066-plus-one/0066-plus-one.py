class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Time complexity: O(n),
        # Space complexity: O(n)
        # new=0
        # for i in digits:
        #     new=new*10+i
        # new=new+1
        # seen=[]
        # for j in str(new):
        #     seen.append(int(j))
        # return seen    

        for i in range(-1,-(len(digits)+1),-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        return [1]+digits
    #   Time complexity: O(n) 
    #   Space complexity: O(1) 
