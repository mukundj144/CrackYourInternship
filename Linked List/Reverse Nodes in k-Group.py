# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head, k):
        prev = None
        current = head
        count = 0
        # Reverse first k nodes
        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        return prev, current  # prev is the new head, current is the next node after the reversed part
    
    def reverseKGroup(self, head, k):
        count = 0
        current = head
        # Count k nodes
        while current and count < k:
            current = current.next
            count += 1
        
        if count == k:
            # Reverse first k nodes
            reversed_head, next_node = self.reverseList(head, k)
            # Recursively reverse the remaining list and connect it to the reversed part
            head.next = self.reverseKGroup(next_node, k)
            return reversed_head
        else:
            # If there are less than k nodes left, return the head as is
            return head   