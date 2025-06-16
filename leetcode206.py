# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        stk=[]
        temp=head
        while temp is not None:
            stk.append(temp.val)
            temp=temp.next
        
        temp=head
        while temp is not None:
            
            temp.val=stk.pop()
            temp=temp.next
        return head