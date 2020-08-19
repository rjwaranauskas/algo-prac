# You need to find the largest value in each row of a binary tree.
#
# Example:
#
# Input:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        layers_dict = {1: []}
        output = []

        def get_children(node: TreeNode, current_layer):
            if not node:
                return
            if current_layer not in layers_dict:
                layers_dict[current_layer] = []
            layers_dict[current_layer].append(node.val)

            if node.left != None or node.right != None:
                get_children(node.left, current_layer + 1)
                get_children(node.right, current_layer + 1)
            if node.left == None and node.right == None:
                # layers_dict[current_layer].append(node.val)
                return

        get_children(root, 1)
        for value in layers_dict.values():
            try:
                output.append(max(value))
            except:
                continue
        return output

        # My old method: Doesn't work since it never goes to the right of a node
        # if not root:return []
        # # queue=collections.deque([(root,1)])
        # # dic=collections.defaultdict(list)
        # output = []
        # output.append(root.val)
        # current_layer_list = []
        # next_layer_list = []
        # main_root = root
        # while root.left != None and root.right != None:
        #     print(Solution.get_children(self, root.left))
        #     print(Solution.get_children(self, root.right))

#             current_layer_list.append(root.val)
#             next_layer_list.append(root.left.val)
#             next_layer_list.append(root.right.val)
#             output.append(max(next_layer_list))
#             next_layer_list = []
#             root = root.left
#             if root.left == None and root.right == None:
#                 root = main_root.right
#                 print(root.val)
#                 continue
#         print(current_layer_list)
#         print(next_layer_list)
#         print(output)

# Copied solution from Leetcode to understand
# class Solution:
#     def largestValues(self, root: TreeNode) -> List[int]:
#         if not root: return []
#         queue = collections.deque([(root, 1)])
#         dic = collections.defaultdict(list)
#         while queue:
#             root, level = queue.popleft()
#             if not root:
#                 continue
#             dic[level].append(root.val)
#             if root.left:
#                 queue.append((root.left, level + 1))
#             if root.right:
#                 queue.append((root.right, level + 1))
#         res = []
#         for key in sorted(dic):
#             res.append(max(dic[key]))
#         return res
