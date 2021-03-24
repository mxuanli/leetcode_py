# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        """
        前序递归，取出所有值，再比较
        :param p:
        :param q:
        :return:
        """
        t_list = list()
        q_list = list()

        def foo(t: TreeNode, node_list: list):
            # 前序递归
            if not t:
                node_list.append(None)
                return
            node_list.append(t.val)
            foo(t.left, node_list)
            foo(t.right, node_list)
        foo(p, t_list)
        foo(q, q_list)
        if t_list == q_list:
            return True
        return False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 递归
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        # 只要上边的判断中出现过false，那么下边的表达式一定为false
        r = self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        return r

    def run(self):
        t1 = TreeNode(1)
        t2 = TreeNode(2)
        t3 = TreeNode(3)
        t1.left = t2
        t1.right = t3
        r1 = TreeNode(1)
        r2 = TreeNode(2)
        r3 = TreeNode(3)
        r1.left = r2
        r1.right = r3
        r = self.isSameTree(t1, r1)
        print(r)


s = Solution()
s.run()
