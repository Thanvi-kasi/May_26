from bisect import bisect_left
from typing import List

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:

        def subset_sums(arr):
            sums = [0]
            for num in arr:
                sums += [s + num for s in sums]
            return sums

        n = len(nums)

        left_sums = subset_sums(nums[:n // 2])
        right_sums = subset_sums(nums[n // 2:])

        right_sums.sort()

        ans = abs(goal)

        for x in left_sums:
            target = goal - x
            idx = bisect_left(right_sums, target)

            if idx < len(right_sums):
                ans = min(ans, abs(x + right_sums[idx] - goal))

            if idx > 0:
                ans = min(ans, abs(x + right_sums[idx - 1] - goal))

        return ans
