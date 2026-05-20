class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # Remove all factors of 2
        while n % 2 == 0:
            n //= 2

        ans = 1
        factor = 3

        # Count divisors of the odd part
        while factor * factor <= n:
            count = 0

            while n % factor == 0:
                n //= factor
                count += 1

            ans *= (count + 1)
            factor += 2

        # If n is still greater than 1, it's a prime factor
        if n > 1:
            ans *= 2

        return ans
