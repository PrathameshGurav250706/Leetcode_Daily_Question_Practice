class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        new = []

        for op in operations:
            if op == "C":
                new.pop()

            elif op == "D":
                new.append(new[-1] * 2)

            elif op == "+":
                new.append(new[-1] + new[-2])

            else:
                new.append(int(op))

        return sum(new)
        # Time complexity: O(n)
        # Space complexity: O(n)