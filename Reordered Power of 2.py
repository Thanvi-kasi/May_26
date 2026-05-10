class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = sorted(str(n))
        
        for i in range(31):  # Powers of 2 up to 10^9
            if sorted(str(1 << i)) == target:
                return True
        
        return False
