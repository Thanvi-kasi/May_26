from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = defaultdict(list)
        for i, num in enumerate(nums):
            mp[num].append(i)

        ans = [0] * len(nums)

        for indices in mp.values():
            n = len(indices)
            prefix = [0] * (n + 1)

            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]

            for i, idx in enumerate(indices):
                left = i * idx - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - (n - i - 1) * idx
                ans[idx] = left + right

        return ans
