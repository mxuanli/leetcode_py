# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node_list = list()
        self.foo(root, node_list)
        root = TreeNode()
        tmp = root
        for n in node_list:
            node = TreeNode(val = n)
            tmp.right = node
            tmp = tmp.right
        return root.right

    def foo(self, root: TreeNode, node_list: list) -> list:
        if not root:
            return node_list
        self.foo(root.left, node_list)
        node_list.append(root.val)
        self.foo(root.right, node_list)
        return node_list