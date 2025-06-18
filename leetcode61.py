# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next or k==0:
            return head
        length=1
        tail=head
        while tail.next:
            tail=tail.next
            length+=1
        k%=length
        if k==0:
            return head
        step_to_new_tail=length-k
        new_tail=head
        for i in range(step_to_new_tail-1):
            new_tail=new_tail.next
        
        new_head=new_tail.next
        new_tail.next=None
        tail.next=head
        return new_head