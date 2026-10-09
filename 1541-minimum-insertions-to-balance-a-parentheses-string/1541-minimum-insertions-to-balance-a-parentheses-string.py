
class Solution(object):
    def minInsertions(self, s):
        open_count = 0
        insertions = 0
        i = 0

        while i < len(s):
            if s[i] == "(":
                open_count += 1
                i += 1
            else:
                # Check for two consecutive closing parentheses
                if i + 1 < len(s) and s[i + 1] == ")":
                    i += 2
                else:
                    # Insert one closing parenthesis
                    insertions += 1
                    i += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    # Insert one opening parenthesis
                    insertions += 1

        # Each unmatched opening parenthesis needs two closing parentheses
        insertions += open_count * 2

        return insertions
