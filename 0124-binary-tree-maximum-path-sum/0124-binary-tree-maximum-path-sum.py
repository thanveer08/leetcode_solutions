# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float("-inf")
        def height(node):
            nonlocal maxi
            if node == None: return 0
            left = max(0,height(node.left))
            right = max(0,height(node.right))
            
            maxi =  max(maxi,node.val+left+right)

            return node.val + max(left,right)
        height(root)
        return maxi    