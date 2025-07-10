# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        """
        q=deque()
        def dfs(root):
            if not root:

                return
            q.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        if q:
            q.popleft()
        
        for i in range(len(q)):
            
            root.right=q.popleft()
            root.left=None
            root=root.right
        
