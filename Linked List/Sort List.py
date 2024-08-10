# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head

        # Split the list into two halves
        mid = self.getMiddle(head)
        left = head
        right = mid.next
        mid.next = None  # Split the list into two halves

        # Sort each half
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge the sorted halves
        return self.merge(left, right)

    def getMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        # Attach the remaining nodes, if any
        if left:
            tail.next = left
        elif right:
            tail.next = right

        return dummy.next
