"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        dict1={}
        while curr:
            node=Node(x=curr.val)
            dict1[curr]=node
            curr=curr.next
        curr=head
        while curr:
            newnode=dict1[curr]
            newnode.next=dict1[curr.next] if curr.next else None
            newnode.random=dict1[curr.random] if curr.random else None
            curr=curr.next
        return dict1[head]
        