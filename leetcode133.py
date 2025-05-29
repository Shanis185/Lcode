"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        start=node
        d={}
        stk=[]
        stk.append(start)
        visited=set()
        visited.add(start)
        while stk:
            node=stk.pop()
            d[node]=Node(val=node.val)
            for neigh in node.neighbors:
                if neigh not in visited:
                    visited.add(neigh)
                    stk.append(neigh)
        for old,new in d.items():
            for neigh in old.neighbors:
                new_neigh=d[neigh]
                new.neighbors.append(new_neigh)
        return d[start]

        