# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp and count<k:
            temp=temp.next
            count+=1
        if count<k:
            return head
        prev=None
        curr=head
        for i in range(k):
            new=curr.next
            curr.next=prev
            prev=curr
            curr=new
        
        head.next=self.reverseKGroup(curr,k)
        return prev