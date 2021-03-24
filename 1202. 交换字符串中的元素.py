from collections import defaultdict


class UnionFindSet:
    """
    并查集类
    """
    def __init__(self):
        self.father = dict()

    def add(self, x):
        # 添加节点
        if x not in self.father:
            self.father[x] = None

    def merge(self, x, y):
        # 合并节点
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.father[rx] = ry

    def is_connected(self, x, y):
        # 判断是否相连
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return True
        return False

    def find(self, x):
        root = x
        # 直到查到找祖先节点，即父节点为空的节点
        while self.father.get(root) is not None:
            root = self.father[root]
        # 压缩
        while x != root:
            father_code = self.father[x]
            self.father[x] = root
            x = father_code
        return root


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: list) -> str:
        """
        换关系具有传递性，使用并差集找出索引链接在一起可以交换的字符，然后分别排序后组合在一起
        :param s:
        :param pairs:
        :return:
        """
        # 创建并查集
        ufs = UnionFindSet()
        for pair in pairs:
            x, y = pair
            ufs.merge(x, y)
        # 获取连通节点（拥有同一个父节点的节点）
        node_list = defaultdict(list)
        for i in range(len(s)):
            father_node = ufs.find(i)
            node_list[father_node].append(i)
        # 字符串是不可改变类型
        s_list = list(s)
        # 分组排序
        for node_v in node_list.values():
            # 排序下标，方便用字典序插入字符
            sort_index = sorted(node_v)
            # 获取对应字符，并排序
            string_list = [s[index_] for index_ in node_v]
            string_list.sort()
            # 交换
            for i in range(len(sort_index)):
                s_list[sort_index[i]] = string_list[i]
        # 合并
        r = "".join(s_list)
        return r

    def run(self):
        s = "dcab"
        pairs = [[0, 3], [1, 2]]
        r = self.smallestStringWithSwaps(s, pairs)
        print(r)


s = Solution()
s.run()
