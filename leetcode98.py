class Solution(object):
    def isValidBST(self, root):
        stk=[]
        current=root
        prev=None
        while current or stk:
            while current:
                stk.append(current)
                current=current.left
            current=stk.pop()
            if prev!=None and current.val<=prev:
                return False

            prev=current.val
            current=current.right
        return True