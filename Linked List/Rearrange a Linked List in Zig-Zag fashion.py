'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def zigzag(self, head_node):
        if not head_node or not head_node.next:
            return head_node
        
        # Initialize pointers
        curr = head_node
        should_less = True  # True means "should be less than or equal to" (odd positions)
        
        while curr and curr.next:
            if (should_less and curr.data > curr.next.data) or (not should_less and curr.data < curr.next.data):
                # Swap the values
                curr.data, curr.next.data = curr.next.data, curr.data
            
            # Move to the next pair and toggle the should_less flag
            curr = curr.next
            should_less = not should_less
        
        return head_node
