# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            
            fast=fast.next.next

            if slow==fast:
                entry=head
                while entry!=slow:
                    slow=slow.next
                    entry=entry.next
                return entry
        return 