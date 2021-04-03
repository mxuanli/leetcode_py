from collections import defaultdict


class MyHashSet2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = defaultdict(bool)

    def add(self, key: int) -> None:
        self.hash[key] = True

    def remove(self, key: int) -> None:
        if self.hash[key]:
            del self.hash[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hash[key]


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        tmp = key % 10
        tmp1 = key // 10
        if not self.set[tmp]:
            self.set[tmp] = [False] * 100001
        self.set[tmp][tmp1] = key

    def remove(self, key: int) -> None:
        tmp = key % 10
        tmp1 = key // 10
        if self.set[tmp] and self.set[tmp][tmp1]:
            self.set[tmp][tmp1] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        tmp = key % 10
        tmp1 = key // 10
        if not self.set[tmp]:
            return False
        if self.set[tmp][tmp1] is False:
            return False
        return True


s = MyHashSet()
s.add(97)
r = s.contains(97)
print(r)
