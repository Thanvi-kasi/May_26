class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_sum = right_sum = 0
        left_q = right_q = 0
        
        # Process left half
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
        
        # Process right half
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
        
        # If total '?' is odd → Alice wins
        if (left_q + right_q) % 2 == 1:
            return True
        
        # Check if Bob can force equality
        return (left_sum - right_sum) != (right_q - left_q) // 2 * 9
