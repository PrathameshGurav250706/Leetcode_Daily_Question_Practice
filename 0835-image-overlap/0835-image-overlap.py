class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        # Shift img1 by (dr, dc)
        for dr in range(-(n - 1), n):
            for dc in range(-(n - 1), n):

                count = 0

                for i in range(n):
                    for j in range(n):

                        # Position in img1 after shifting
                        ni = i + dr
                        nj = j + dc

                        # Check if shifted position is inside the matrix
                        if 0 <= ni < n and 0 <= nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                count += 1

                ans = max(ans, count)

        return ans