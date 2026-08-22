# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
class Solution:
    def _init_(self):
        self.ans = []
    def inorder(self, root):
        #base case
        if root is None:
            return

        # recursive case
        # self.ans.append(root.val)
        self.inorder(root.left) # left subtree
        self.ans.append(root.val)
        self.inorder(root.right) # right subtree
        # self.ans.append(root.val)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.inorder(root)
        return self.ans