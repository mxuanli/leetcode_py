# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        node_dict = dict()

        def foo(root):
            # 转换成{子节点: 父节点}的格式
            if root == None:
                return
            if root.left != None:
                node_dict[root.left.val] = root
                foo(root.left)
            if root.right != None:
                node_dict[root.right.val] = root
                foo(root.right)

        foo(root)
        r = list()

        def find(root, from_node, step):
            # 深度优先搜索，from_node避免重复搜索
            if root == None:
                return
            if step == k:
                r.append(root.val)
                return
            if root.left != from_node:
                find(root.left, root, step + 1)
            if root.right != from_node:
                find(root.right, root, step + 1)
            if node_dict.get(root.val) != None and node_dict.get(root.val) != from_node:
                find(node_dict[root.val], root, step + 1)

        find(target, None, 0)

        return r

