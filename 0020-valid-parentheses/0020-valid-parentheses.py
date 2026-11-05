class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()

                if i==")" and top!="(":
                    return False
                if i=="]" and top!="[":
                    return False
                if i=="}" and top!="{":
                    return False
        return len(stack)==0
# Time Complexity: O(n) – We traverse the string exactly once.
# Space Complexity: O(n) – In the worst case, all characters are opening brackets and are stored in the stack.