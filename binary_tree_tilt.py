# https://leetcode.com/problems/binary-tree-tilt/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        all_sums = []
        current_sum = []

        # queue = collections.deque([root])
        # print(queue)
        def find_node_tilt(node: TreeNode):
            if not node:
                return
            if node.left == None and node.right == None:
                all_sums.append(0)
                return

            if node.left == None:
                leftvar = 0
            else:
                leftvar = node.left.val
            if node.right == None:
                rightvar = 0
            else:
                rightvar = node.right.val
            all_sums.append(abs(leftvar - rightvar))
            current_sum = abs(leftvar - rightvar)

            if node.left != None or node.right != None:
                find_node_tilt(node.left)
                find_node_tilt(node.right)
            # if node.left == None and node.right == None:
            #     return

        find_node_tilt(root)
        # print(all_sums)
        return sum(all_sums)

#         1
#        / \
#     2       3
#   /   \    / \
#   4   NULL 5  NULL
#
# [TreeNode{val: 1,
#           left: TreeNode{val: 2,
#                          left: TreeNode{val: 4,
#                                         left: None, right: None}, right: None},
#
# right: TreeNode
# {val: 3, left:
#     TreeNode{val: 5, l
#     eft: None, right: None}, right: None}}
#


# Alternative recursion solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findTilt(self, root: TreeNode) -> int:
#         self.res = 0
#
#         def find_node_tilt(node: TreeNode):
#             if not node:
#                 return 0
#             else:
#                 left = find_node_tilt(node.left)
#                 right = find_node_tilt(node.right)
#                 self.res += abs(left - right)
#                 return node.val + left + right
#
#         find_node_tilt(root)
#         print(self.res)
#         return self.res

