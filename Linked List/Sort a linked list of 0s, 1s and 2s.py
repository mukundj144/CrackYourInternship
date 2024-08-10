class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sort(self, head):
        # Step 1: Extract node values into an array
        values = []
        current = head
        while current:
            values.append(current.data)
            current = current.next
        
        # Step 2: Sort the array
        values.sort()
        
        # Step 3: Rebuild the linked list from the sorted array
        sorted_head = None
        sorted_tail = None
        for value in values:
            new_node = Node(value)
            if sorted_head is None:
                sorted_head = new_node
                sorted_tail = sorted_head
            else:
                sorted_tail.next = new_node
                sorted_tail = new_node
        
        return sorted_head
