class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_of_multiples(k):
            m = n // k
            return k * m * (m + 1) // 2
        
        return (
            sum_of_multiples(3)
            + sum_of_multiples(5)
            + sum_of_multiples(7)
            - sum_of_multiples(15)
            - sum_of_multiples(21)
            - sum_of_multiples(35)
            + sum_of_multiples(105)
        )
