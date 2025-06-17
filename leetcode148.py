# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk=[]
        curr=head
        while curr:
            stk.append(curr.val)
            curr=curr.next
        stk.sort(reverse=True)
        curr=head
        for i in range(len(stk)):
            curr.val=stk.pop()
            curr=curr.next
        return head
