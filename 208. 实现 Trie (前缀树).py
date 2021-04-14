class Node:

    def __init__(self):
        self.child = dict()
        self.is_word = False  # 判断有没有作为最后一个字符(跟节点到当前节点是否形成有效字符串)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if not node.child.get(i):
                node.child[i] = Node()
            node = node.child[i]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if not node.child.get(i):
                return False
            node = node.child[i]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if not node.child.get(i):
                return False
            node = node.child[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

t = Trie()
r = t.insert("apple")
print(r)
r = t.search("apple")
print(r)
r = t.search("app")
print(r)
