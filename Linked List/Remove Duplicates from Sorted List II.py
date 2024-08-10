# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # Move the current pointer as long as we have duplicates
            while current.next and current.val == current.next.val:
                current = current.next
            
            # If prev.next is current, it means no duplicates detected
            if prev.next == current:
                prev = prev.next
            else:
                # Skip all duplicates
                prev.next = current.next
            
            current = current.next
        
        return dummy.next
