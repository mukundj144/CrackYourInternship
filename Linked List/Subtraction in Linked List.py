class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def remove_leading_zeros(head):
    while head and head.data == 0:
        head = head.next
    return head if head else Node(0)

def is_greater_or_equal(l1, l2):
    l1 = remove_leading_zeros(l1)
    l2 = remove_leading_zeros(l2)
    
    # Convert linked lists to integers for comparison
    def to_int(node):
        result = 0
        while node:
            result = result * 10 + node.data
            node = node.next
        return result
    
    return to_int(l1) >= to_int(l2)

class Solution:
    def subLinkedList(self, l1, l2):
        # Remove leading zeros
        l1 = remove_leading_zeros(l1)
        l2 = remove_leading_zeros(l2)
        
        # Ensure l1 >= l2
        if not is_greater_or_equal(l1, l2):
            l1, l2 = l2, l1
        
        # Reverse both linked lists
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        head = None
        temp = None
        borrow = 0
        
        # Subtract linked lists
        while l1 or l2:
            sub = (l1.data if l1 else 0) - (l2.data if l2 else 0) - borrow
            if sub < 0:
                sub += 10
                borrow = 1
            else:
                borrow = 0
            
            # Create new node for the result
            new_node = Node(sub)
            
            if head is None:
                head = new_node
                temp = head
            else:
                temp.next = new_node
                temp = temp.next
            
            # Move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Reverse the result to get the final subtraction result
        head = reverse(head)
        
        # Remove leading zeros
        head = remove_leading_zeros(head)
        
        return head