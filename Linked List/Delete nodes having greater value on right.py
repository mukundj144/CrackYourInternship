'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        #Your code here
        if not head:
            return None
        
        # Reverse the linked list
        head = self.reverse(head)
        
        # Initialize the max_value with the value of the new head
        max_value = head.data
        current = head
        
        # Traverse the reversed list
        while current and current.next:
            if current.next.data < max_value:
                # Delete the next node
                current.next = current.next.next
            else:
                # Update max_value and move to the next node
                current = current.next
                max_value = current.data
        
        # Reverse the list again to restore original order
        head = self.reverse(head)
        
        return head
        
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev