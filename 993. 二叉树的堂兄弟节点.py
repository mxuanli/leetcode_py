# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def foo(node, tar, depth, parent):
            if not node:
                return 0, parent
            if node.val == tar:
                return depth, parent
            level, parent = foo(node.left, tar, depth + 1, node)
            if level == 0:
                level, parent = foo(node.right, tar, depth + 1, node)
            return level, parent

        depth1, p1 = foo(root, x, 0, None)
        depth2, p2 = foo(root, y, 0, None)
        return depth1 == depth2 and p1 != p2
