class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)

        def next(i):
            # 下一次的位置
            return (i + nums[i]) % n  # 当出界时，把位置变成前边的值

        for i in range(n):
            slow = i  # 慢指针
            fast = next(i)  # 快指针
            while nums[i] * nums[fast] > 0 and nums[i] * nums[next(fast)] > 0:  # 同正为正，同负为负，保证同号
                if slow == fast:
                    # 判断是否环长度k为1，再向后走一次，如果和当前值相同就为一
                    if slow == next(slow):
                        break
                    return True
                # 快慢指针
                slow = next(slow)
                fast = next(fast)
                fast = next(fast)
        return False
