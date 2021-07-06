# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def foo(left: TreeNode, right: TreeNode):
            # 左右都为空返回True
            if not left and not right:
                return True
            # 只有一个为空返回False
            if not left or not right:
                return False
            # 值不一样返回False
            if left.val != right.val:
                return False
            return foo(left.left, right.right) and foo(right.left, left.right)

        return foo(root.left, root.right)
