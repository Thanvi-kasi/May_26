class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = fast = i

            while True:
                nxt_slow = next_index(slow)
                if (nums[slow] > 0) != direction or (nums[nxt_slow] > 0) != direction:
                    break

                nxt_fast = next_index(fast)
                if (nums[fast] > 0) != direction or (nums[nxt_fast] > 0) != direction:
                    break

                nxt_fast2 = next_index(nxt_fast)
                if (nums[nxt_fast2] > 0) != direction:
                    break

                slow = nxt_slow
                fast = nxt_fast2

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            cur = i
            while nums[cur] != 0 and (nums[cur] > 0) == direction:
                nxt = next_index(cur)
                nums[cur] = 0
                cur = nxt

        return False
