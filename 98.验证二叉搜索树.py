# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.left_node = None

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 访问左，如果左边不是二叉搜索树，就返回False
        if not self.isValidBST(root.left):
            return False
        # 访问当前，prev是左边的节点，如果左边比当前大，就返回False
        if self.left_node != None and self.left_node.val >= root.val:
            return False
        # 访问右节点之前，把当前节点设置为左节点
        self.left_node = root
        # 访问右，如果右边不是二叉搜索树，就返回False
        if not self.isValidBST(root.right):
            return False
        return True
