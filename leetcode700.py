# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res=[]
        ans=[]
        def dfs(root):
            if not root:
                return
            if root.val==val:
                ans.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans[0] if ans else None