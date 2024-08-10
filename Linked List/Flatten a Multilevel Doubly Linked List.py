# class Node:
#     def __init__(self, val, prev=None, next=None, child=None):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flatten_dfs(node):
            # If node is None, return None
            if not node:
                return None
            
            # Pointers to traverse the list
            current = node
            last = None
            
            while current:
                # If there is a child node, we need to process it
                if current.child:
                    # Flatten the child list
                    child_head = flatten_dfs(current.child)
                    
                    # Save the next node
                    next_node = current.next
                        
                    # Connect the current node to the flattened child list
                    current.next = child_head
                    child_head.prev = current
                    
                    # Traverse to the end of the child list
                    last = child_head
                    while last.next:
                        last = last.next
                    
                    # Connect the end of the child list to the saved next node
                    last.next = next_node
                    if next_node:
                        next_node.prev = last
                    
                    # Remove the child pointer
                    current.child = None
                
                # Move to the next node
                last = current
                current = current.next
            
            return node
        
        return flatten_dfs(head)
