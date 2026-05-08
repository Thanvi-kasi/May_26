class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        nums.sort()
        
        ans = 0
        prefix = 0
        
        for x in nums:
            x2 = (x * x) % MOD
            
            ans = (ans + x2 * (x + prefix)) % MOD
            
            prefix = (2 * prefix + x) % MOD
        
        return ans
