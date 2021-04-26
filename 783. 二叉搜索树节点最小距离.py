# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def foo(root):
            if not root:
                return
            foo(root.left)
            tmp.append(root.val)
            foo(root.right)

        tmp = list()
        foo(root)
        r = max(tmp)
        for i in range(1, len(tmp)):
            r = min(r, tmp[i] - tmp[i - 1])
        return r
