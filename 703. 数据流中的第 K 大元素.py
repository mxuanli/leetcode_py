import heapq


class KthLargest:

    def __init__(self, k: int, nums: list):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums )

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:  # 小根队，删除所有小的
            heapq.heappop(self.nums)
        return self.nums[0]

k = 3
nums = [4, 5, 8, 2]
kt = KthLargest(k, nums)
r = kt.add(3)
print(r)
r = kt.add(4)
print(r)
r = kt.add(5)
print(r)
r = kt.add(8)
print(r)
r = kt.add(2)
print(r)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)