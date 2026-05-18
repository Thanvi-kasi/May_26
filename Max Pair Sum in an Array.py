class Solution:
    def maxSum(self, nums: list[int]) -> int:
        best = {}
        ans = -1

        for num in nums:
            # Find largest digit in num
            max_digit = max(str(num))

            # If same largest digit already exists
            if max_digit in best:
                ans = max(ans, best[max_digit] + num)
                best[max_digit] = max(best[max_digit], num)
            else:
                best[max_digit] = num

        return ans
