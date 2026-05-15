from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        longest = 0

        for num in freq:
            if num + 1 in freq:
                longest = max(longest, freq[num] + freq[num + 1])

        return longest
