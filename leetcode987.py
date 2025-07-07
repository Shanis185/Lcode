# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        dictt=defaultdict(list)
        def dfs(root,row,col):
            
            if not root:
                return
            dictt[col].append((row,root.val))
            dfs(root.left,row+1,col-1)
            dfs(root.right,row+1,col+1)
            

            
        dfs(root,0,0)
        for i in sorted(dictt.keys()):
            column_nodes=sorted(dictt[i],key=lambda x:(x[0],x[1]))
        
            res.append([val for row,val in column_nodes])
        return res

