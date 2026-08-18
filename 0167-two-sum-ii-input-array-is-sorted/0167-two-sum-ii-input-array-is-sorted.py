class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range(len(numbers)):
            diff=target-numbers[i]

            if diff in seen:
                return [seen[diff],i+1]
            
            seen[numbers[i]]=i+1
        return []