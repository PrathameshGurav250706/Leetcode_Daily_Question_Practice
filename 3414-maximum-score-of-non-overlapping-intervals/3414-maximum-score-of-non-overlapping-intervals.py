class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append([l, r, w, i])

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # next[i] = first interval whose start > arr[i].right
        import bisect

        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect.bisect_right(
                starts, arr[i][1]
            )

        # dp[i][k] = best result from i onward
        # when we can still choose k intervals.
        #
        # Store (score, indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # Option 1: don't choose this interval
                not_take = dp[i + 1][k]

                # Option 2: choose this interval
                ni = next_idx[i]
                take_score = arr[i][2] + dp[ni][k - 1][0]
                take_indices = [arr[i][3]] + dp[ni][k - 1][1]

                take = (take_score, sorted(take_indices))

                # Choose better result
                if take_score > not_take[0]:
                    dp[i][k] = take
                elif take_score < not_take[0]:
                    dp[i][k] = not_take
                else:
                    # Same score -> lexicographically smaller indices
                    dp[i][k] = min(take, not_take)

        return dp[0][4][1]