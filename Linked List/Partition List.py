# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right=ListNode(),ListNode()
        ltrail=left
        rtrail=right

        while head:
            if head.val<x:
                ltrail.next=head
                ltrail=ltrail.next
            else:
                rtrail.next=head
                rtrail=rtrail.next    
            head=head.next

        ltrail.next=right.next
        rtrail.next=None
        return left.next        