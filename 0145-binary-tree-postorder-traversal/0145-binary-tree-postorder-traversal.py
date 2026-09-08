# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def f(Treenode):
            if Treenode == None:
                return
            f(Treenode.left)
            f(Treenode.right)
            res.append(Treenode.val)
        f(root)
        return res    