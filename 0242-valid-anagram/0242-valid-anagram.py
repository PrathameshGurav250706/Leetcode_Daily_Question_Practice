class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # first=sorted(s)
        # second=sorted(t)
        # if first==second:
        #     return True
        # return False
        # Overall time complexity: O(n log n). The space complexity is O(n) 
        if len(s) != len(t):
            return False

        first={}
        second={}
        for i in s:
            if i in first:
                first[i]+=1
            else:
                first[i]=1
        for j in t:
            if j in second:
                second[j]+=1
            else:
                second[j]=1
        for key in first:
            if first[key] != second.get(key,0):
                return False

        return True
#         Time complexity:
# - Building the first frequency map: O(n), where n is len(s).
# - Building the second frequency map: O(m), where m is len(t).
# - Comparing counts: at most O(k) where k is the number of distinct keys in first (k ≤ n).

# Overall time complexity: O(n + m).

# Space complexity:
# - Storing two frequency maps, each up to the number of distinct characters in the respective string. In the worst case, O(n + m) extra space. If the alphabet is bounded (e.g., constant size), the space reduces to O(1) with respect to input length.