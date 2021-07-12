class Solution:

    def __init__(self, nums: List[int]):
        self.list = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.list

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        copy_list = self.list[:]
        random.shuffle(copy_list)
        return copy_list

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
