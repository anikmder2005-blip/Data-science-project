# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         result = []
#         queue = collections.deque([root])
#         left_to_right = True
#         while queue:
#             level_size = len(queue)
#             level_nodes = collections.deque()
#             for _ in range(level_size):
#                 node = queue.popleft()
#                 if left_to_right:
#                     level_nodes.append(node.val)
#                 else:
#                     level_nodes.appendleft(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if left_to_right:
#                     queue.append(node.right)
#             result.append(list(level_nodes))
#             left_to_right = not left_to_right
#         return result
from typing import Optional, List
import collections

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        queue = collections.deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = collections.deque()

            for _ in range(level_size):
                node = queue.popleft()

                # Zigzag direction
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)

                # Always add both children
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(list(level_nodes))

            # Change direction
            left_to_right = not left_to_right

        return result