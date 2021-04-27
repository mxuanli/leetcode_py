# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        r = 0

        def foo(root: TreeNode, low: int, high: int, r: int) -> int:
            v = 0
            if not root:
                return r
            if low <= root.val <= high:
                v = root.val
            l = foo(root.left, low, high, r)
            r = foo(root.right, low, high, r)
            return r + l + v

        r = foo(root, low, high, r)
        return r


class Solution2:

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        r = 0
        if not root:
            return r
        if low <= root.val <= high:
            r += root.val
        if root.val < high:
            r += self.rangeSumBST(root.right, low, high)
        if root.val > low:
            r += self.rangeSumBST(root.left, low, high)
        return r
