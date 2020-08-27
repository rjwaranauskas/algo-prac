# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.res = None
        def find_node(node: TreeNode):
            if not node: return None
            if node.val == val:
                self.res = node
                return node
            else:
                find_node(node.left)
                find_node(node.right)
        find_node(root)
        print(self.res)
        return self.res